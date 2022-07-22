# Acima da diagonal Principal:
# Esse programa realizar uma operação de Soma ou média em uma matriz[12][12]

# Subprogramas
def realizarOperacao(caractere, matriz):# Função que realiza a soma ou a média de uma linha da lista.
    antigaMatriz = []
    for lista in matriz:
        for valor in lista:
            antigaMatriz.append(valor)
    if (caractere == 'S'):
         print(f'{sum(antigaMatriz):.1f}')
    elif(caractere == 'M'):
        print(f'{sum(antigaMatriz)/len(antigaMatriz):.1f}')
    return None

def gerarMatriz(colunas, linhas):# Função geradora da matriz
    matriz = [None] * colunas
    for espaco in range(len(matriz)):# Gera a matiriz de acordo com os parametros
        listaAux = []
        if (len(listaAux) == linhas):
            listaAux.clear()
        while (len(listaAux) < linhas):# Gera as listas da matriz
            numero = float(input())
            listaAux.append(numero)
        matriz[espaco] = listaAux
    return matriz

def diagonalDaMatriz(): # Função com os parametros e comandados e execução
    colunasDaMatriz = 3
    linhasDaMatriz = 3
    operacao = input()
    matriz = gerarMatriz(colunasDaMatriz, linhasDaMatriz)
    finalIntervalo = 1
    for lista in matriz:
        del(lista[0:finalIntervalo])
        finalIntervalo += 1
    realizarOperacao(operacao, matriz)
    return None

# Programa Principal
diagonalDaMatriz()