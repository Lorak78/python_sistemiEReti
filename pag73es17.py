import math
def main():
    numero = int(input("inserisci fino a quale potenza di 2 visualizzare: "))
    esponente = int(math.log2(numero))
    listaPotenze = [2**num for num in range(esponente + 1) if (2**num <= numero)]
    print(listaPotenze)

def main1():
    nPotenze2 = int(input("inserisci quante potenze di due vuoi visualizzare: "))
    listaPotenze2 = [2**num for num in range(nPotenze2 + 1)]
    print(listaPotenze2)



if __name__ == "__main__":
    main()