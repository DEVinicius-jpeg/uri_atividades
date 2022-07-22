def gerarLista(lista):
    while(len(lista) < 10):
        indice = lista[-1]
        lista.append(indice * 2)
    return lista

lista = []
valor = int(input())
lista.append(valor)

for posicao, numero in enumerate(gerarLista(lista)):
    print(f"N [{posicao}] = {numero}")
