#Matriz Quadrada II
#Este Programa construi uma matriz de acordo com as entradas do usuario

#Subprogramas
def criaMatriz(N):#Função geradora da matriz
    matriz = []
    for element in range(1, (N + 1)):
        matrizAux = []
        count = element
        for num in range(N):
            matrizAux.append(abs(count))
            if (count == 1):
                count -= 3
            else:
                count -= 1
        matriz.append(matrizAux)
    return matriz

def imprimiBonito(N, matriz):#Função responsavel por imprimir a matriz na formatação correta
    for elemente in range(N):
        texto = ''
        for num in range(N):
            texto += " %3d" % matriz[elemente][num]
        print(texto[1:])
    print("")

#Programa Principal
N = int(input())
while(N !=0):
    imprimiBonito(N, criaMatriz(N))
    N = int(input())