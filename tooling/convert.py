import os
import subprocess
import re
import sys
import importlib

'''
    converter
    surprisingly badly documented for one of my scripts.. sorry.
    - it is 'documented in code', I suppose.
'''
sourceDir = '../tooling/bdf-sources'
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

sources = os.listdir(sourceDir)
#sources = os.listdir(sourceDir)[0:10] # good for test and debug


badFontFiles = []
generated = 0


def doFont(base, cset, bodycount):
    charset = outDir + '/' + cset + '-char.set'
    infile = sourceDir + '/' + base + '.bdf'
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
    files = response.split('===============================================\n')
    if len(files) != 2:
        #print('{} - Bad response from bdf2py'.format(cset))
        # Just skip... ignore fails here
        return True
    fontheight = 0
    fontfamily = ''
    for line in files[0].split('\n'):
        if re.match('^Declared family:',line):
            fam = line[16:].strip().replace(' ','-')
            fam = 'generic' if fam == 'None' else fam
            fontfamily = fam if len(fam) > 0 else 'generic'
        if re.match('^Height',line):
            fontheight = int(line.split(' ')[1])
    if fontheight == 0:
        print(files[0])
        print(' {} (bad font return)'.format(cset), end='')
        return True
    print(' ' + cset, end='')
    outname = '{}_{:02d}_{}_{}'.format(prefix, fontheight, base.replace('-','_'), cset)
    packageInfo(base, infile, outname, cset, fontheight, fontfamily, files)
    return True

def packageInfo(base, infile, outfile, cset, fontheight, fontfamily, files):
    global generated
    body = files[1].split('\n')[7:]
    for bod in bodycount:
        if body == bod:
            # already covered by a previous charset, skip
            print('-', end='')
            return
    bodycount.append(body)
    print('+', end='')
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
    with open(outMapDir + '/' + outfile + '.map','w') as i:
        i.write(files[0])
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
        for line in files[1]:
            f.write(line)

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
print('Font File: charsets')
for file in sources:
    if file[-4:] != '.bdf':
        #print('Not BDF:',file)
        continue
    baseName = file[:-4]
    for matchfonts in sets.fonts:
        if re.match(matchfonts, baseName):
            print(file,end=' :')
            bodycount = []
            for ch in sets.charsets.keys():
                if not doFont(baseName, ch, bodycount):
                    # HardFail here == bad .bdf file/format, skip to next font
                    break
            print()

'''
    Wrap up and summary
'''

print('\nProcessed ' + str(generated) + ' font files that match and have compatible .bdf format')
if generated == 0:
    print('None! (check settings and errors, try changing debug to True)')
    exit()
