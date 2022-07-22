def proximoNumero(lista, num):
    while(len(lista) < max(num)+1):
        ultimaPosicao = lista[len(lista) - 1]
        penultimaPosicao = lista[len(lista) - 2]
        soma = ultimaPosicao + penultimaPosicao
        lista.append(soma)
    return None

def gerarFibonacci():
    casoDeTestes = int(input())
    fibonacci =[0,1,1]
    numfib = []
    while(len(numfib) < casoDeTestes):
        valor = int(input())
        numfib.append(valor)
    proximoNumero(fibonacci,numfib)
    for valor in numfib:
        print(f"Fib({valor}) = {fibonacci[valor]}")


gerarFibonacci()