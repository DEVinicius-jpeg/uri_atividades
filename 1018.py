valorLido = int(input())

print(valorLido)
if (valorLido // 100 >= 1):
    print(valorLido // 100, "nota(s) de R$ 100,00")
else:
    print(0, "nota(s) de R$ 100,00")

if ((valorLido % 100) // 50 >= 1):
    print((valorLido % 100) // 50, "nota(s) de R$ 50,00")
else:
    print(0, "nota(s) de R$ 50,00")

if (((valorLido % 100) % 50) // 20 >= 1):
    print(((valorLido % 100) % 50) // 20, "nota(s) de R$ 20,00")
else:
    print(0, "nota(s) de R$ 20,00")

if ((((valorLido % 100) % 50) % 20) // 10 >= 1):
    print((((valorLido % 100) % 50) % 20) // 10, "nota(s) de R$ 10,00")
else:
    print(0, "nota(s) de R$ 10,00")

if (((((valorLido % 100) % 50) % 20) % 10) // 5 >= 1):
    print(((((valorLido % 100) % 50) % 20) % 10) // 5, "nota(s) de R$ 5,00")
else:
    print(0, "nota(s) de R$ 5,00")

if ((((((valorLido % 100) % 50) % 20) % 10) % 5) // 2 >= 1):
    print((((((valorLido % 100) % 50) % 20) % 10) % 5) // 2, "nota(s) de R$ 2,00")
else:
    print(0, "nota(s) de R$ 2,00")

if (((((((valorLido % 100) % 50) % 20) % 10) % 5) % 2) // 1 >= 1):
    print(((((((valorLido % 100) % 50) % 20) % 10) % 5) % 2) // 1, "nota(s) de R$ 1,00")
else:
    print(0, "nota(s) de R$ 1,00")