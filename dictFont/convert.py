import os
import subprocess
import re
import sys

'''
    converter
    surprisingly badly documented for one of my scripts.. sorry.
    - it is 'documented in code', I suppose.
'''
sourceDir = '../u8g2/tools/font/bdf'
outDir = '.'
prefix = 'dictFont_'
# provide debug argument to see the return from bdfToDict runs
debug = sys.argv[1] if len(sys.argv) > 1 else False

#sources = os.listdir(sourceDir)
sources = os.listdir(sourceDir)[11:64] # good for test and debug

charsets = {
            'n':bytes([32] + [37] + list(range(40,59)) + [176]),
            't':bytes([32] + [43] + [45] + [46] +list(range(48,59))),
            'e':bytes(list(range(32,256))),
            'r':bytes(list(range(32,128))),
            'u':bytes(list(range(32,96))),
            }
'''
'''

includeList = [
                '^cour',
                '^helv',
                '^ncen',
                '^px',
                '^tim',
                '^font_tiny',
                '^tom-thumb',
                '^spleen',
                '^symb',
                '^u8g2',
                '^u8x8',
                '^u8glib',
                '^emoticons',
                '^battery',
                '^freedoom',
                '^7Segments',
                '^7_Seg',
                '^unifont$',
                '^\\d+x\\d+$',  # X11 fonts
                '^micro$`',
                '^cursor$',
               ]

specialsets = {
                    '^battery':[32,48],
                    '^7_seg':[70,77],
                    }

ignoredFontFiles = []
badFontFiles = []
generated = {}


def doFont(base, cset):
    charset = outDir + '/' + cset + '-char.set'
    inFile = sourceDir + '/' + base + '.bdf'
    outFile = prefix + base.replace('-','_') + '_' + cset + '.py'
    cmd = 'python bdfToDict.py ' + inFile + ' ' + charset
    if debug:
        cmd += ' True'
    run = subprocess.run(cmd, shell=True, capture_output=True)
    if debug:
        print('\nsubprocess return::\n', run)
    if run.returncode != 0:
        if os.path.exists('tmp_' + outFile):
            os.remove('tmp_' + outFile)
        print('\nFail: ',run.stdout.decode('latin-1').strip(), end="")
        return True  # a softfail
    # DEBUG
    print('\n' + cset, end=' : ')
    print(run.stdout.decode('latin-1').strip(),end='')
    return True
    # DEBUG
    fontHeight = int(run.stdout.split(b'\n')[3].split(b' ')[2])
    packageInfo(base,infile,fileName,fontHeight)
    return True

def includeFont(name):
    # looks 'name' up against a list of allowed font patterns, return True if OK
    for fam in includeList:
        if re.match(fam,name):
            return True
    return False

def packageInfo(base,infile,fileName,fontHeight):
    global generated
    copyrightTxt = []
    commentTxt = []
    f = open(infile,'r')
    for line in f:
        if re.match('^ *COPYRIGHT',line):
            copyrightTxt.append(line)
        if re.match('^ *COMMENT',line):
            commentTxt.append(line)
    if base not in generated.keys():
        generated[base] = [fontHeight]
    generated[base].append(fileName)
    outSubDir = outDir + '/' + str(fontHeight)
    os.makedirs(outSubDir, exist_ok=True)
    if os.path.exists(outSubDir + '/' + fileName):
        # clean for overwrite
        os.remove(outSubDir + '/' + fileName)
    if debug:
        print('PostProcessing:', 'tmp_' + fileName)
    tmp = open('tmp_' + fileName,'r')
    ffile = open(outSubDir + '/' + fileName,'w')
    ffile.write("'''\n")
    ffile.write('    ' + fileName + ' : generated as part of the microPyEZfonts repository\n')
    ffile.write('      https://github.com/easytarget/microPyEZfonts\n\n')
    ffile.write('    Original ' + base + '.bdf font file was sourced from the U8G2 project:\n')
    ffile.write('      https://github.com/olikraus/u8g2\n\n')
    ffile.write('    This font definition can be used with the "writer" class from Peter Hinches\n')
    ffile.write('      micropython font-to-py tool, and was generated using his tooling from\n')
    ffile.write('      https://github.com/peterhinch/micropython-font-to-py\n\n')
    ffile.write('    Original Copyright Notice from source:\n\n')
    if len(copyrightTxt) > 0:
        for line in copyrightTxt:
            ffile.write('    ' + line)
    else:
        ffile.write('    None found:\n')
    ffile.write('\n    Original Comments from source (may include copyright info):\n\n')
    if len(commentTxt) > 0:
        for line in commentTxt:
            ffile.write('    ' + line)
    else:
        ffile.write('    None found:\n')
    ffile.write("'''\n\n")
    for line in tmp:
        ffile.write(line)
    tmp.close()
    ffile.close()
    os.remove('tmp_' + fileName)

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
print('Font File: charsets ("*" = sparse, "+" = full)')
for file in sources:
    if file[-4:] != '.bdf':
        print('Not BDF:',file)
    baseName = file[:-4]
    if not includeFont(baseName):
        ignoredFontFiles.append(str(file))
        continue
    print(file,end=':')
    for chrs in charsets.keys():
        if not doFont(baseName,chrs):
            # HardFail here == bad .bdf file/format, skip to next font
            break
    print()

'''
    Wrap up and summary
'''

def height(e):
    return generated[e][0]

print('\nProcessed ' + str(len(generated)) + ' font files that match and have compatible .bdf format')
if len(generated) == 0:
    print('None! (check settings and errors, try changing debug to True)')
    exit()
list = list(generated.keys())
list.sort(key=height)
total = 0
for font in list:
    if debug:
        print(str(generated[font][0]) + 'px : ' + font)
    for file in generated[font][1:]:
        if debug:
            print('    ' + file)
        total += 1
print('\nProcessed ' + str(len(generated)) + ' font files into ' + str(total) +  ' variants.')
