#Combinador
#Combina duas strings em orden intercalada de seus caracteres

#Subprogramas
def combinarTexto(texto):
    primeiroTexto, segundoTexto = texto.split()
    textoCombinado = ''
    contador = 0
    while contador < len(primeiroTexto) and contador < len(segundoTexto):
        textoCombinado += primeiroTexto[contador] + segundoTexto[contador]
        contador += 1
    if contador < len(primeiroTexto):
        textoCombinado += primeiroTexto[contador:]
    elif contador < len(segundoTexto):
        textoCombinado += segundoTexto[contador:]
    print(textoCombinado)


#Programa Principal
casosDeTeste = int(input())
for caso in range(casosDeTeste):
    combinarTexto(texto = input())