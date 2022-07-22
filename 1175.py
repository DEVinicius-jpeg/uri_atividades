def alteraValorLista(lista):
  segundaLista = []
  controle = 19

  while (len(segundaLista) < 20):
    segundaLista.append(lista[controle])
    controle = controle - 1
  return segundaLista

primeiraLista = [None] * 20

for element in range(len(primeiraLista)):
  primeiraLista[element] = int(input())

for posicao, value in enumerate(alteraValorLista(primeiraLista)):
  print(f"N[{posicao}] = {value}")