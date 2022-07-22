"""while(True):
    d, n = input().split()
    if(d == '0' and n == '0'):
        break
    n = '0' + n
    v = int(n.replace(d,''))
    print(v)"""

d, n = input().split()

while (d != '0' and n != '0'):
    textoNovo = n.replace(d, '')
    if (textoNovo == ''):
        textoNovo = 0
    print(int(textoNovo))
    d, n = input().split()