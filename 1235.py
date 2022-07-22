casosDeTestes = int(input())

for caso in range(casosDeTestes):
    entrada = input()
    comprimento = int(len(entrada)/2) -1
    saida = entrada[comprimento::-1] + entrada[len(entrada)-1:comprimento:-1]
    print(saida)
