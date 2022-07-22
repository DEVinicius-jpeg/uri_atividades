casosDeTestes = int(input())

for caso in range(casosDeTestes):
    n = input()
    leds = 0
    for letra in n:
        if (letra == '1'):
            leds += 2
        elif (letra == '2' or letra == '3' or letra =='5'):
            leds += 5
        elif (letra == '4'):
            leds += 4
        elif (letra == '6' or letra == '9' or letra == '0' ):
            leds += 6
        elif (letra == '7'):
            leds += 3
        elif (letra == '8'):
            leds += 7
    print(leds, 'leds')

