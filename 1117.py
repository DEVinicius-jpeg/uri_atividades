def verificaNota(nota):
    if (nota < 0 or nota > 10 ):
        print('nota invalida')
        return None
    else:
        return nota

notas = []

while(len(notas) < 2):
    notaAluno = float(input())
    nota = verificaNota(notaAluno)
    if(nota != None):
        notas.append(nota)

print(f"media = {(notas[0] + notas[1]) / 2:.2f}")
