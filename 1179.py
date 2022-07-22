# Preenchimento de Vetor:
# Esse programa separa as entradas dos usuarios em listas pares e impares. As listas só podem ter 5 vetores.

#Subprogramas
def printarLista(lista): #Função responsavel por printar a saída.
    for posicao, valor in enumerate(lista):
        if(valor % 2 == 0):#Verifica se a lista é par, para dar a saída correta.
            print(f"par[{posicao}] = {valor}")
        else:
            print(f"impar[{posicao}] = {valor}")
    return None

def separarNumerosEmListas(): #Função responsavel por inserir os valores nas listas correta.
    vetorPar = []
    vetorImpar = []
    for indice in range(1,16): #Loop para pegar entrada do usuario.
        numero = int(input())
        if (numero % 2 == 0):#A entrada é par? Se sim, entra no if.
            if(len(vetorPar) < 5):
                vetorPar.append(numero)
            else:
                printarLista(vetorPar)
                vetorPar.clear()
                vetorPar.append(numero)
        else:# Se não é par, é impar, então cai no else.
            if(len(vetorImpar) < 5):
                vetorImpar.append(numero)
            else:
                printarLista(vetorImpar)
                vetorImpar.clear()
                vetorImpar.append(numero)
    #Imprime a lista quando os casos de testes são finalizados.
    printarLista(vetorImpar)
    printarLista(vetorPar)
    return None

#Programa Principal
separarNumerosEmListas()
