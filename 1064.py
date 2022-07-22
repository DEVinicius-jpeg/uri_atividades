valores = [None] * 6
contador = 0
soma = 0

for element in range(len(valores)):
    valores[element] = float(input())

for valor in valores:
    if (valor > 0):
        contador = contador + 1
        soma = soma + valor

print(f"{contador} valores positivos")
print("%.1f"%(soma/contador))