notas = input().split()
nota1 = float(notas[0]) * 2
nota2 = float(notas[1]) * 3
nota3 = float(notas[2]) * 4
nota4 = float(notas[3]) * 1

mediaPonderada = (nota1 + nota2 + nota3 + nota4) / 10

print("Media:", "%.1f"%(mediaPonderada) )

if (mediaPonderada >= 7.0):
    print("Aluno aprovado.")
elif(mediaPonderada < 5.0):
    print("Aluno reprovado.")
elif (5.0 <= mediaPonderada <= 6.9):
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame:", "%.1f"%(notaExame))
    notaNova = (mediaPonderada + notaExame) /2
    if (notaNova >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:", "%.1f"%(notaNova))


