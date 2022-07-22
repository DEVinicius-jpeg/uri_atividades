def gerarVetor(tamanho):
    vetor = []
    elemento = list(map(int, input().split()))
    for num in elemento:
        if (len(vetor) < tamanho):
            vetor.append(num)
    return vetor

def localizarInf():
    tamanhoVetor = int(input())
    vetor = gerarVetor(tamanhoVetor)
    for posicao, valor in enumerate(vetor):
        if(valor == min(vetor)):
            print(f"Menor valor: {valor}")
            print(f"Posicao: {posicao}")
    return None

localizarInf()