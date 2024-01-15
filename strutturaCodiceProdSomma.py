def somma(a,b):
    #pass
    return a + b

def prodotto(a,b):
    #pass
    return a * b

def divisione(a, b):
    return a / b

def sottrazione(a,b):
    return a - b

def main():
    dizionario = {"+": somma, "*": prodotto, "/": divisione, "-": sottrazione}
    operazione = input("scrivi + per somma * per prodotto / per divisione - per sottrazione")
    a = float(input("Scrivi il primo numero: "))
    b = float(input("Scrivi il primo numero: "))
    print(dizionario[operazione](a, b))

if __name__ == "__main__":
    main()