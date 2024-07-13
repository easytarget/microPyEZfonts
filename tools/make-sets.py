import os
import subprocess
import re
import sys
import importlib

'''
    Utility to build font sets based on a local 'sets.py' file that
    defines source fonts and charsets.

    surprisingly badly documented for one of my scripts.. sorry.
    - it is 'documented in code', I suppose.
'''
outDir = '.'
prefix = 'ezFBfont'

# provide debug argument to see the return from bdfToDict runs
debug = sys.argv[1] if len(sys.argv) > 1 else False

# import sets definition
if not os.path.isfile('sets.py'):
    print('This script must be run in a folder that contains "sets.py"')
    exit()
sys.path.append(os.getcwd())
sets = importlib.import_module('sets', package=None)

tooldir = os.path.dirname(os.path.realpath(__file__))
tool = tooldir + '/../bdf2dict.py'
if not os.path.isfile(tool):
    print('Cannot find "bdf2dict.py" in:', tooldir + '/..')
    exit()

sources = os.listdir(sets.sourceDir)
#sources = os.listdir(sets.sourceDir)[0:10] # good for test and debug

badFontFiles = []
generated = 0


def doFont(base, infile, cset):
    charset = outDir + '/' + cset + '-char.set'
    files = []
    cmd = 'python {} {} _ {}'.format(tool, infile, charset)
    if debug:
        cmd += ' debug'
    run = subprocess.run(cmd, shell=True, capture_output=True)
    if debug:
        print('\nsubprocess return::\n', run)
    if run.returncode != 0:
        if debug:
            print('\nFail: ',run.stdout.decode('latin-1').strip(), end="")
        return True  # a softfail

    response = run.stdout.decode('latin-1')
    if not os.path.isfile('_' + base + '.py'):
        if debug:
            print('\nFail: {}'.format(response), end="")
        return True  # a softfail

    # examine the map file for basic info
    fontheight = 0
    fontfamily = ''
    with open('_' + base + '.map','r') as ffile:
        for line in ffile.read().split('\n'):
            if re.match('^Declared family:',line):
                fam = line[16:].strip().replace(' ','-')
                fam = '' if fam == 'None' else fam
                fontfamily = fam if len(fam) > 0 else 'generic'
            elif re.match('^Height',line):
                fontheight = int(line.split(' ')[1])
            elif re.match('^Char ',line):
                # no point scanning whole file..
                break

    if fontheight == 0:
        print(' {} (bad font return)'.format(cset), end='')
        return True
    print(' ' + cset, end='', flush=True)
    outname = '{}_{:02d}_{}_{}'.format(prefix, fontheight, base.replace('-','_'), cset)
    packageInfo(base, infile, outname, cset, fontheight, fontfamily)
    os.remove('_' + base + '.py')
    os.remove('_' + base + '.map')
    os.remove('_' + base + '.set')
    return True

def packageInfo(base, infile, outfile, cset, fontheight, fontfamily):
    global generated
    with open('_' + base + '.set', 'r') as thisset:
        contains = thisset.read()
    for previous in priorsets:
        if contains == previous:
            # already covered by a previous charset, skip
            print('-', end='', flush=True)
            return
    priorsets.append(contains)
    print('+', end='', flush=True)
    generated += 1
    outSubDir = '{}/{}/{}'.format(outDir, fontfamily, cset)
    os.makedirs(outSubDir, exist_ok=True)
    outMapDir = '{}/maps'.format(outSubDir)
    os.makedirs(outMapDir, exist_ok=True)
    if os.path.exists(outSubDir + '/' + outfile):
        # clean for overwrite
        os.remove(outSubDir + '/' + outfile)
    if debug:
        print('PostProcessing:', outfile)
    with open('_' + base + '.map', 'r') as m:
        with open(outMapDir + '/' + outfile + '.map','w') as o:
            o.write(m.read())
    with open(outSubDir + '/' + outfile + '.py','w') as f:
        f.write("'''\n")
        f.write('    ' + outfile + ' : generated as part of the microPyEZfonts repository\n')
        f.write('      https://github.com/easytarget/microPyEZfonts\n\n')
        f.write('    This font definition can be used with the "ezFBfont" class provided there.\n')
        f.write('    It can also be used with the "writer" class from Peter Hinches micropython\n')
        f.write('      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py\n\n')
        f.write('    Original ' + base + '.bdf font file was sourced from the U8G2 project:\n')
        f.write('      https://github.com/olikraus/u8g2\n\n')
        f.write("'''\n")
        with open('_' + base + '.py', 'r') as s:
            f.write(s.read())

def safe_module_name(name):
    for s in "!@#$%^&*()+-={}[]:;'<>?,.~":
        name = name.replace(s, '_')
    return name

# init

os.makedirs(outDir,exist_ok=True)

# create our charset files:
for s in sets.charsets.keys():
    if sets.charsets[s] is None:
        continue
    cfile = outDir + '/' + s + '-char.set'
    with open(cfile,'wb') as f:
        for c in sets.charsets[s]:
            f.write(chr(c).encode("utf-8", "replace"))

# loop the font files
sources.sort()
print('Font File: valid charsets (+:generated, -:duplicate skipped')
for file in sources:
    if file[-4:] != '.bdf':
        #print('Not BDF:',file)
        continue
    baseName = safe_module_name(file[:-4])
    print(file, end=' :', flush=True)
    priorsets = []
    for ch in sets.charsets.keys():
        if not doFont(baseName, sets.sourceDir + '/' + file, ch):
            # HardFail here == bad .bdf file/format, skip to next font
            break
    print()

# clean up sets files
for s in sets.charsets.keys():
    if sets.charsets[s] is None:
        continue
    cfile = outDir + '/' + s + '-char.set'
    os.remove(cfile)

# Wrap up and summary
print('\nProcessed ' + str(generated) + ' font files that match and have compatible .bdf format')
if generated == 0:
    print('None! (check settings and errors, try changing debug to True)')
    exit()
