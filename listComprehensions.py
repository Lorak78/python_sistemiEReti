#list comprehension
#lista con i primi 5 quadrati perfetti
import random
def main():
    quadrati = [i**2 for i in range(1, 6)] #simbolo di potenza: **, i**2 con i in intervallo 1 a 6
    print(quadrati)
    #lista con i primi 12 numeri interi
    interi = [i for i in range(12)]
    #lista di stringhe
    stringhe = ["computer", "cellulare", "laptop"]
    stringhe_c = [parola for parola in stringhe if parola[0] == "c"]
    print(stringhe_c)
    #10 voti a caso da 2 a 10
    voti = [random.randint(2, 10) for _ in range(10)]
    print(voti)
    voti_insuff = [voto for voto in voti if voto < 6]
    print(voti_insuff)

if __name__ == "__main__":
    main()