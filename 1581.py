N = int(input())
while (N > 0):
    N = N - 1
    lingua = []
    k = int(input())
    while (k > 0):
        k = k - 1
        lingua.append(input())
    qtd = lingua[0]
    for k in lingua:
        if k != qtd:
            qtd = 'ingles'
    print(qtd)
