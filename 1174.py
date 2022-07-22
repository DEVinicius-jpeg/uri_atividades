def geraValoresVetor(lista):
    while(len(lista) < 100):
        numero = float(input())
        lista.append(numero)
    return lista

A = []

for posicao, value in enumerate(geraValoresVetor(A)):
    if (value <= 10):
        print(f"A[{posicao}] = {value:.1f}")
