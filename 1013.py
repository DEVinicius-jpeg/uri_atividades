def ehMaior (a, b):
    maiorAb = (a + b + abs(a-b)) /2
    return int(maiorAb)

valores = input().split()

umValor = int(valores[0])
doisValores = int(valores[1])
tresValores = int(valores[2])

primeiraAnalise = ehMaior(umValor, doisValores)

segundaAnalise = ehMaior(primeiraAnalise, tresValores)

print(f"{segundaAnalise} eh o maior")

