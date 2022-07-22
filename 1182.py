# Coluna na Matriz:
# Esse programa realizar uma operação de Soma ou média em uma matriz[12][12]

# Subprogramas
def realizarOperacao(caractere, matriz, matrizColuna):# Função que realiza a soma ou a média de uma coluna da lista.
    coluna = []
    if (caractere == 'S'):
        for numero in matriz:
            coluna.append(numero[matrizColuna])
        print(f'{sum(coluna):.1f}')
    elif(caractere == 'M'):
        for numero in matriz:
            coluna.append(numero[matrizColuna])
        print(f'{sum(coluna)/len(coluna):.1f}')
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

def linhaNaMatriz(): # Função com os parametros e comandados de execução
    colunasDaMatriz = 12
    linhasDaMatriz = 12
    colunaAnalisada = int(input())
    operacao = input()
    matriz = gerarMatriz(colunasDaMatriz, linhasDaMatriz)
    realizarOperacao(operacao, matriz, colunaAnalisada)
    return None

# Programa Principal
linhaNaMatriz()