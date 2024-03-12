import os
import subprocess
import re
'''
    converter
'''
sourceDir = 'u8g2/tools/font/bdf'
outDir = 'mpy-fonts'
prefix = 'mpyFbFont_u8g2_'

sources = os.listdir(sourceDir)
#sources = os.listdir(sourceDir)[:20] # good for debug

charsets = {
            'e':None,
            'f':bytes(list(range(32,127)) + list(range(160,256))).decode("latin-1"),
            'r':bytes(list(range(32,127))).decode("latin-1"),
            'n':bytes([32] + list(range(42,59))).decode("latin-1"),
            'u':bytes(list(range(32,96))).decode("latin-1"),
            }

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
                '^unifont',
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
    global generated,badFontFiles
    infile = sourceDir + '/' + base + '.bdf'
    if chars == 'e':
        charset = ''
    else:
        charset = '-k ' + chars + '-char.set '
    fileName = prefix + base + '_' + chars + '.py'
    cmd = 'micropython-font-to-py/font_to_py.py -x ' + charset + infile + ' 0 tmp_' + fileName
    if not checkValid(infile):
        badFontFiles.append(str(base))
        return False  # a hardfail
    run = subprocess.run(cmd, shell=True, capture_output=True)
    if run.returncode != 0:
        return True  # a softfail
    realHeight = int(run.stdout.split(b'\n')[3].split(b' ')[2])
    # log
    if base not in generated.keys():
        generated[base] = [realHeight]
    generated[base].append(fileName)
    outSubDir = outDir + '/' + str(realHeight)
    os.makedirs(outSubDir, exist_ok=True)
    if os.path.exists(outSubDir + '/' + fileName):
        os.remove(outSubDir + '/' + fileName)
    os.rename('tmp_' + fileName, outSubDir + '/' + fileName)
    print(' ' + chars, end='')
    return True

def includeFont(name):
    # looks 'name' up against a list of allowed font patterns, return True if OK
    # all 'vanilla' u8g2 fonts go in
    #if re.match('^\\d+x\\d+$',name):
    #    return True
    for fam in includeList:
        if re.match(fam,name):
            return True
    return False
'''
    init
'''
# (re)create our charset files:
for s in charsets.keys():
    if charsets[s] is None:
        continue
    c = s + '-char.set'
    o = open(c,'w')
    o.write(charsets[s])
    o.close()

'''
    main loop
'''
os.makedirs(outDir,exist_ok=True)
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
            # HardFail here == bad .bdf file/format
            break
    print()

#print('Ignored:\n',ignoredFontFiles)

if len(badFontFiles) > 0:
    print('\nUnsupported/Bad:')
    for file in badFontFiles:
        print(file)

def height(e):
    return generated[e][0]

print('\nGenerated font files: (' + str(len(generated)) + ')')
if len(generated) == 0:
    print('None: check settings and errors')
    exit()
list = list(generated.keys())
list.sort(key=height)
total = 0
for font in list:
    print(str(generated[font][0]) + 'px : ' + font)
    for file in generated[font][1:]:
        print('    ' + file)
        total += 1
print('\nProcessed ' + str(len(generated)) + ' font files into ' + str(total) +  ' variants.')
