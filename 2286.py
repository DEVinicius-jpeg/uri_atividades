casoTeste = int(input())
teste = 0
while(casoTeste != 0):
    jogadorPar = input()
    jogadorImpar = input()
    teste += 1
    print(f"Teste {teste}")
    for numero in range(casoTeste):
        primeiraEntrada, segundaEntrada = map(int, input().split())
        if ((primeiraEntrada + segundaEntrada) % 2 == 0):
            print(jogadorPar)
        else:
            print(jogadorImpar)
    casoTeste = int(input())
    print()