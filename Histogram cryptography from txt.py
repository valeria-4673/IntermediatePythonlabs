from os import strerror
try:
    dicti = {}
    s = open ('sample.txt', 'rt')
    ch_1 = s.read(1)
    while ch_1 != '':
        ch_1 = ch_1.upper()
        if ch_1 not in dicti.keys():
            dicti[ch_1] = 1
        else:
            dicti[ch_1] += 1
        ch_1 = s.read(1)
    s.close()
    print('El diccionario es: ',dicti)
except IOError as e:
        print('Upss', strerror(e.errno))

try:
    outi = open('outi.txt', 'wt')
    sorted_dict = dict(sorted(dicti.items(), key= lambda item: item[1], reverse=True))
    print(sorted_dict)
    for key, value in sorted_dict.items():
        outi.write( key + '-->' + str(value))
    outi.close()
except IOError as e:
        print('Upss escribiendo', strerror(e.errno))
