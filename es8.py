def main():
    operaz = int(input("che operazione vuoi eseguire?(0: addizione, 1: sottrazione, 2: moltiplicazione, 3: divisione): "))
    n1 = int(input("inserisci il primo numero: "))
    n2 = int(input("inserisci il secondo numero: "))
    if operaz == 0:
        ris = n1 + n2
    elif operaz == 1:
        ris = n1 - n2
    elif operaz == 2:
        ris = n1 * n2
    elif operaz == 3:
        if n2 == 0:
            print("impossibile")
        else:
            ris = n1 / n2
    if operaz != 3 and n2 != 0:
        print(f"risultato: {ris}")

    

if __name__ == "__main__":
    main()