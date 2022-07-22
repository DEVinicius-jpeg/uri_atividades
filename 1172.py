def substituiValores(lista):
    for element, value in enumerate(lista):
        if value <= 0:
            lista[element] = 1
    return lista

vetor = []

while(len(vetor) < 10):
    valor = int(input())
    vetor.append(valor)

for posicao, numero in enumerate(substituiValores(vetor)):
    print(f"X[{posicao}] = {numero}")
