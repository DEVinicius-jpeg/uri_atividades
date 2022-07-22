senha = 2002
acertou = 0

while (acertou == 0):
    tentativa = int(input())
    if (tentativa != senha):
        print("senha Invalida")
    else:
        print("Acesso Permitido")
        acertou = 1

