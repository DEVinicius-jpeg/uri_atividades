# Linha na Matriz:
# Esse programa realizar uma operação de Soma ou média em uma matriz[12][12]

# Subprogramas
def realizarOperacao(caractere, linha):# Função que realiza a soma ou a média de uma linha da lista.
    if (caractere == 'S'):
         print(f'{sum(linha):.1f}')
    elif(caractere == 'M'):
        print(f'{sum(linha)/len(linha):.1f}')
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

def linhaNaMatriz(): # Função com os parametros e comandados e execução
    colunasDaMatriz = 12
    linhasDaMatriz = 12
    linhaAnalisada = int(input())
    operacao = input()
    matriz = gerarMatriz(colunasDaMatriz, linhasDaMatriz)
    realizarOperacao(operacao, matriz[linhaAnalisada])
    return None

# Programa Principal
linhaNaMatriz()