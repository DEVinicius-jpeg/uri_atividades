#O jogo matemático de Paula
#De acordo com a entrada analisa o tipo de operação a ser realizada, soma, subtração e multiplicação

#Subprogramas
def jogoMatematico(entrada): #Função que analisa a entrada para determinar o tipo de operação na saida
    if entrada[0] == entrada[2]:
        print(int(entrada[0]) * int(entrada[2]))
    elif ord(entrada[1]) >= 65 and ord(entrada[1]) <= 90:
        print(int(entrada[2]) - int(entrada[0]))
    else:
        print(int(entrada[2]) + int(entrada[0]))

#Programa Principal
casosDeTeste = int(input())
for caso in range(casosDeTeste):
    jogoMatematico(entrada=input())