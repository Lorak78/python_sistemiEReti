#fare un programma che chiede 2 numeri float, stampare una stringa con i 2
#numeri in ordine decrescente
n1 = float(input("inserisci il primo numero"))
n2 = float(input("inserisci il secondo numero"))
if n1 < n2:
    n1, n2 = n2, n1
stringa = f"numero maggiore: {n1}, numero minore {n2}"
print(stringa)