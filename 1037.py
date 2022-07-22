valorQualquer = float(input())

if (valorQualquer >= 0 and valorQualquer <= 25.0000):
    print("Intervalo [0,25]")
else:
    if (valorQualquer > 25 and valorQualquer <= 50):
        print("Intervalo (25,50]")
    else:
        if (valorQualquer > 50 and valorQualquer <= 75):
            print("Intervalo (50,75]")
        else:
            if (valorQualquer > 75 and valorQualquer <= 100):
                print("Intervalo (75,100]")
            else:
                print("Fora de intervalo")
