import os
import subprocess
import re
import sys

'''
    converter
    surprisingly badly documented for one of my scripts.. sorry.
    - it is 'documented in code', I suppose.
'''
sourceDir = 'source-fonts'
outDir = 'testing'
prefix = 'dictFont_'
# provide debug argument to see the return from bdfToDict runs
debug = sys.argv[1] if len(sys.argv) > 1 else False

sources = os.listdir(sourceDir)
#sources = os.listdir(sourceDir)[11:64] # good for test and debug

charsets = {
            't':bytes([32] + [43] + [45] + [46] + list(range(48, 59))),
            'n':bytes([32] + [37] + list(range(40, 59)) + [176]),
            'u':bytes(list(range(32, 96))),
            'r':bytes(list(range(32, 127))),
            'x':bytes(list(range(160, 256))),
            'e':bytes(list(range(32, 127)) + list(range(160, 256))),
            }
'''
'''

badFontFiles = []
generated = 0


def doFont(base, cset):
    charset = outDir + '/' + cset + '-char.set'
    infile = sourceDir + '/' + base + '.bdf'
    outname = prefix + base.replace('-','_') + '_' + cset
    cmd = 'python bdf2dict.py ' + infile + ' ' + charset + ' True'
    if debug:
        cmd += ' True'
    run = subprocess.run(cmd, shell=True, capture_output=True)
    if debug:
        print('\nsubprocess return::\n', run)
    if run.returncode != 0:
        print('\nFail: ',run.stdout.decode('latin-1').strip(), end="")
        return True  # a softfail

    response = run.stdout.decode('latin-1')
    files = response.split('===============================================\n')
    if len(files) != 2:
        #print('{} - Bad response from bdf2py'.format(cset))
        return True
    fontheight = 0
    for line in files[0].split('\n'):
        if re.match('^Height: ',line):
            fontheight = int(line.split(' ')[1])
    if fontheight == 0:
        print('{} - Bad summary response from bdf2py'.format(cset))
        return True
    packageInfo(base, infile, outname, fontheight, files)
    return True

def packageInfo(base, infile, outfile, fontheight, files):
    global generated
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
    outSubDir = outDir + '/' + str(fontheight)
    os.makedirs(outSubDir, exist_ok=True)
    if os.path.exists(outSubDir + '/' + outfile):
        # clean for overwrite
        os.remove(outSubDir + '/' + outfile)
    if debug:
        print('PostProcessing:', outfile)
    with open(outSubDir + '/' + outfile + '.info','w') as i:
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
for s in charsets.keys():
    if charsets[s] is None:
        continue
    cfile = outDir + '/' + s + '-char.set'
    with open(cfile,'wb') as f:
        f.write(charsets[s])

'''
    main loop
'''
sources.sort()
print('Font File: charsets')
for file in sources:
    if file[-4:] != '.bdf':
        print('Not BDF:',file)
    baseName = file[:-4]
    print(file,end=':')
    for chrs in charsets.keys():
        print(' ' + chrs, end='')
        if not doFont(baseName, chrs):
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
