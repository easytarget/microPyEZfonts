from sys import argv, modules, implementation
from gc import collect, mem_free

def test(p):
    def m(s):
        collect()
        o = mem_free()
        print('{}: {}'.format(s,o), end=', ')
        return o

    def h(t,s):
        r = s.read(1000)
        if len(r) > 0:
            t.write(r)
            return True
        return False
    
    print('{}:: '.format(p),end='')
    b = m('start')
    try:
        tfont = __import__(p)
    except MemoryError as e:
        print('fail: {}'.format(e))
        return
    a = m('import')
    print('F:' if tfont.monospaced() else 'V:',end='')
    for c in range(tfont.min_ch(),tfont.max_ch()+1):
        g,_,_ = tfont.get_ch(chr(c))
        if g is not None:
            print('.',end='')
    del g
    m('run')
    del tfont
    del modules[p]
    print()
    return b-a

# tests
tlist = [
    ['size:6', 'mPyEZfont_u8g2_4x6_r','ezFBfont_06_4x6_ascii'],
    ['size:14', 'mPyEZfont_u8g2_timB10_r','ezFBfont_14_timB10_ascii'],
    ['size:23', 'mPyEZfont_u8g2_spleen_12x24_r','ezFBfont_23_spleen_12x24_ascii'],
    ['size:33', 'mPyEZfont_u8g2_timB24_r','ezFBfont_33_timB24_ascii'],
    ['set:time', 'mPyEZfont_u8g2_courB14_t','ezFBfont_12_courB14_time'],
    ['set:num', 'mPyEZfont_u8g2_courB14_n','ezFBfont_16_courB14_num'],
    ['set:ascii', 'mPyEZfont_u8g2_courB14_r','ezFBfont_17_courB14_ascii'],
    ['set:full', 'mPyEZfont_u8g2_courB14_e','ezFBfont_20_courB14_full'],
]

# run tests
used = []
for i in tlist:
    used.append([i[0], test(i[1]), test(i[2])])

# show results
print('\nResults:')
outfmt = '{:10} : {:>7}  {:>7}'
print(outfmt.format('test','bin','dict'))
print(outfmt.format('-----','-----','-----'))
for i in used:
    print(outfmt.format(i[0],i[1],i[2]))
print('\n{}'.format(implementation))