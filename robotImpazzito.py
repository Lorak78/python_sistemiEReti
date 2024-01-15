import random 

def spostamenti(lista = [1, -1]): #passaggio di parametri con valori di default
    return random.choice(lista)

def main():
    timeInSecondi = 60 * 60 * 24 * 5
    list_spostamenti = [random.choice([1, -1]) for _ in range(timeInSecondi)]
    sommaSpost = 0
    for spostamento in list_spostamenti:
        sommaSpost += spostamento
    print(f"{timeInSecondi} e la somma e' {sommaSpost}")

if __name__ == "__main__":
    main()