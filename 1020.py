idadePessoa = int(input())

if (idadePessoa // 365 > 0):
    print(idadePessoa // 365, "ano(s)")
else:
    print(0,"ano(s)")

if ((idadePessoa % 365) // 30 > 0):
    print((idadePessoa % 365) // 30, "mes(es)")

if (((idadePessoa % 365) % 30) < 30 ):
    print(((idadePessoa % 365) % 30) // 1, "dia(s)")