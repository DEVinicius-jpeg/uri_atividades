#Ordenação por tamanho
# Ordenação de strings do maior para o menor

#Subprogramas
def ordenarFrase(frase):
    listaDePalavras = list(map(str, frase.split()))
    listaDePalavras.sort(key=len, reverse=True)
    for elemente in range(len(listaDePalavras)):
        print(listaDePalavras[elemente], end= ' ')
        if elemente != len(listaDePalavras)-1:
            print('', end= '')
    print()

#Programa Principal
casoDeTeste = int(input())
for numero in range(casoDeTeste):
    ordenarFrase(frase = input())