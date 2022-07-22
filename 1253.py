repeticoes = int(input())

while (repeticoes > 0):
    cifra = input()
    casas = int(input())
    converteLetra = ''
    for letra in cifra:
        numeroLetra = ord(letra) - casas
        if (numeroLetra < 65):
            converteLetra += chr(91 - (65 - numeroLetra))
        else:
            converteLetra += chr(ord(letra) - casas)
    print(converteLetra)
    repeticoes -= 1