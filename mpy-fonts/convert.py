import os
import subprocess
import re
'''
    converter
    surprisingly badly documented for one of my scripts.. sorry.
    - it is 'documented in code', I suppose.
'''
sourceDir = '../u8g2/tools/font/bdf'
outDir = '.'
fontTool = '../micropython-font-to-py/font_to_py.py'
prefix = 'mPyEZfont_u8g2_'
debug = False  # see the return from font_to_py runs

sources = os.listdir(sourceDir)
#sources = os.listdir(sourceDir)[61:74] # good for test and debug

charsets = {
            'e':bytes(list(range(32,255))).decode("latin-1"),
            'r':bytes(list(range(32,127))).decode("latin-1"),
            'n':bytes([32] + [37] + list(range(40,59)) + [176]).decode("latin-1"),
            't':bytes([32] + [43] + [45] + [46] +list(range(48,59))).decode("latin-1"),
            }
'''
unused:
'f':bytes(list(range(32,127)) + list(range(160,256))).decode("latin-1"),
'u':bytes(list(range(32,96))).decode("latin-1"),
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

ignoredFontFiles = []
badFontFiles = []
generated = {}


def checkValid(file):
    res = subprocess.run('grep "^CHARS " ' + file, shell=True, capture_output=True)
    if res.returncode == 0:
        return True
    else:
        return False

def doFont(base,chars='e'):
    global badFontFiles
    charset = '-k ' + outDir + '/' + chars + '-char.set '
    infile = sourceDir + '/' + base + '.bdf'
    if not checkValid(infile):
        badFontFiles.append(str(base))
        return False  # a hardfail, the font file is bad or the wrong version.
    fileName = prefix + base.replace('-','_') + '_' + chars + '.py'
    cmd = fontTool + ' -x ' + charset + '-e 32 ' + infile + ' 0 tmp_' + fileName
    run = subprocess.run(cmd, shell=True, capture_output=True)
    if debug:
        print('\nsubprocess return::\n', run)
    if run.returncode != 0:
        return True  # a softfail
    fontHeight = int(run.stdout.split(b'\n')[3].split(b' ')[2])
    packageInfo(base,infile,fileName,fontHeight)
    print(' ' + chars, end='')
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
    c = outDir + '/' + s + '-char.set'
    o = open(c,'w')
    o.write(charsets[s])
    o.close()


'''
    main loop
'''
sources.sort()
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
#print('Ignored:\n',ignoredFontFiles)

if len(badFontFiles) > 0:
    print('\nUnsupported/Bad:')
    for file in badFontFiles:
        print(file)

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
