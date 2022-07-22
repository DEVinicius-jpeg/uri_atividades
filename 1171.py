def removeRepitidos(lista):
    valores = []
    for element in lista:
        if element not in valores:
            valores.append(element)
    valores.sort()
    return valores

def geraLista(qtd):
    numeros = [None] * qtd
    for element in range(len(numeros)):
        numeros[element] = int(input())
    for valor in removeRepitidos(numeros):
        cont = numeros.count(valor)
        print(f"{valor} aparece {cont} vez(es)")


casodeTeste = int(input())
geraLista(casodeTeste)