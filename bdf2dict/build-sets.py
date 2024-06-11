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
if not os.path.isfile(tooldir + '/bdf2dict.py'):
    print('Cannot find "bdf2dict.py" in:', tooldir)
    exit()

sources = os.listdir(sets.sourceDir)
#sources = os.listdir(sets.sourceDir)[0:10] # good for test and debug


badFontFiles = []
generated = 0


def doFont(base, cset):
    charset = outDir + '/' + cset + '-char.set'
    infile = sets.sourceDir + '/' + base + '.bdf'
    files = []
    cmd = 'python {}/bdf2dict.py {} {} True'.format(tooldir, infile, charset)
    if debug:
        cmd += ' True'
    run = subprocess.run(cmd, shell=True, capture_output=True)
    if debug:
        print('\nsubprocess return::\n', run)
    if run.returncode != 0:
        if debug:
            print('\nFail: ',run.stdout.decode('latin-1').strip(), end="")
        return True  # a softfail

    response = run.stdout.decode('latin-1')
    if not os.path.isfile(base + '.py'):
        print('{}'.format(response))
        # ignore fails here
        return True

    # examine the map file for basic info
    fontheight = 0
    fontfamily = ''
    with open(base + '.map','r') as ffile:
        for line in ffile.read().split('\n'):
            if re.match('^Declared family:',line):
                fam = line[16:].strip().replace(' ','-')
                fam = '' if fam == 'None' else fam
                fontfamily = fam if len(fam) > 0 else 'generic'
            elif re.match('^Height',line):
                fontheight = int(line.split(' ')[1])
            elif re.match('^Char',line):
                # no point scanning whole file..
                break

    if fontheight == 0:
        print(' {} (bad font return)'.format(cset), end='')
        return True
    print(' ' + cset, end='', flush=True)
    outname = '{}_{:02d}_{}_{}'.format(prefix, fontheight, base.replace('-','_'), cset)
    packageInfo(base, infile, outname, cset, fontheight, fontfamily)
    os.remove(base + '.py')
    os.remove(base + '.map')
    os.remove(base + '.set')
    return True

def packageInfo(base, infile, outfile, cset, fontheight, fontfamily):
    global generated
    with open(base + '.set', 'r') as thisset:
        contains = thisset.read()
    for previous in priorsets:
        if contains == previous:
            # already covered by a previous charset, skip
            print('-', end='', flush=True)
            return
    priorsets.append(contains)
    print('+', end='', flush=True)
    generated += 1
    copyrightTxt = []
    commentTxt = []
    with open(infile,'r') as f:
        for line in f:
            if re.match('^ *COPYRIGHT',line):
                copyrightTxt.append(line)
            if re.match('^ *NOTICE',line):
                commentTxt.append(line)
            if re.match('^ *COMMENT',line):
                commentTxt.append(line)
    outSubDir = '{}/{}/{}'.format(outDir, fontfamily, cset)
    os.makedirs(outSubDir, exist_ok=True)
    outMapDir = '{}/maps'.format(outSubDir)
    os.makedirs(outMapDir, exist_ok=True)
    if os.path.exists(outSubDir + '/' + outfile):
        # clean for overwrite
        os.remove(outSubDir + '/' + outfile)
    if debug:
        print('PostProcessing:', outfile)
    with open(base + '.map', 'r') as m:
        with open(outMapDir + '/' + outfile + '.map','w') as i:
            i.write(m.read())
    with open(outSubDir + '/' + outfile + '.py','w') as f:
        f.write("'''\n")
        f.write('    ' + outfile + ' : generated as part of the microPyEZfonts repository\n')
        f.write('      https://github.com/easytarget/microPyEZfonts\n\n')
        f.write('    This font definition can be used with the "ezFBfont" class provided there.\n')
        f.write('    It can also be used with the "writer" class from Peter Hinches micropython\n')
        f.write('      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py\n\n')
        f.write('    Original ' + base + '.bdf font file was sourced from the U8G2 project:\n')
        f.write('      https://github.com/olikraus/u8g2\n\n')
        f.write('    Original Copyright information from source:\n')
        if len(copyrightTxt) > 0:
            for line in copyrightTxt:
                f.write('    ' + line)
        else:
            f.write('    None found\n')
        f.write('\n    Original Comments and Notices from source:\n')
        f.write('    (may include copyright and trademark info):\n')
        if len(commentTxt) > 0:
            for line in commentTxt:
                f.write('    ' + line)
        else:
            f.write('    None found\n')
        f.write("'''\n")
        with open(base + '.py', 'r') as s:
            f.write(s.read())

'''
    init
'''
os.makedirs(outDir,exist_ok=True)

# (re)create our charset files:
for s in sets.charsets.keys():
    if sets.charsets[s] is None:
        continue
    cfile = outDir + '/' + s + '-char.set'
    with open(cfile,'wb') as f:
        for c in sets.charsets[s]:
            f.write(chr(c).encode("utf-8", "replace"))

'''
    main loop
'''
sources.sort()
print('Font File: valid charsets (+:generated, -:duplicate skipped')
for file in sources:
    if file[-4:] != '.bdf':
        #print('Not BDF:',file)
        continue
    baseName = file[:-4]
    print(file,end=' :', flush=True)
    priorsets = []
    for ch in sets.charsets.keys():
        if not doFont(baseName, ch):
            # HardFail here == bad .bdf file/format, skip to next font
            break
    print()

'''
    Wrap up and summary
'''

# clean up sets files
for s in sets.charsets.keys():
    if sets.charsets[s] is None:
        continue
    cfile = outDir + '/' + s + '-char.set'
    os.remove(cfile)

print('\nProcessed ' + str(generated) + ' font files that match and have compatible .bdf format')
if generated == 0:
    print('None! (check settings and errors, try changing debug to True)')
    exit()
