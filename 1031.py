def gerarSalto(n ,m):
    salto = 0
    i = 1
    while (i < n):
        salto = (salto + m) % i
        i += 1
    return salto

n = int(input())

while(n != 0):
    m = 1
    while((gerarSalto(n,m) + 2) != 13):
        m += 1
    print(m)
    n = int(input())