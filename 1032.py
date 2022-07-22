import math
def calculaProximoPrimo(num):
    achou = False
    n = num + 1
    if (n == 2 or n == 3):
        return n
    while (not achou):
        achouDivisor = False
        for i in range(2, math.ceil(n**1/2 + 0.1)):
            if (n % i == 0):
                achouDivisor = True
                break
        if (not achouDivisor):
            achou = True
        else:
            n += 1
    return n
n = int(input())
numerosPrimos = []
while(n!=0):
    while (len(numerosPrimos) < n):
        proximoPrimo = numerosPrimos[-1] if len(numerosPrimos) > 0 else 1
        numerosPrimos.append(calculaProximoPrimo(proximoPrimo))
    jogadores = [k + 1 for k in range (n)]
    i = 0
    pos = (numerosPrimos[i] - 1) % len(jogadores)
    while (len(jogadores) > 1):
        jogadores.pop(pos)
        i += 1
        pos = (pos + numerosPrimos[i] - 1) % len(jogadores)
    print(jogadores[0])
    n = int(input())