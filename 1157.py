def divisores(num):
    divisores = []
    for i in range(1, num//2+1):
        if num % i == 0: 
            divisores.append(i)
    divisores.append(num)
    return divisores

num = int(input())
for element in divisores(num):
    print(element)

