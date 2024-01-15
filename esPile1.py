#LE PILE IN PYTHON
def push(p, elem):
    p.append(elem)

def pop(p):
    if len(p) > 0:
        x = p.pop()
    else:
        x = None
    return x

def main():
    parentesi_aperte = ["{", "[", "("]
    parentesi_chiuse = ["}", "]", ")"]
    stringa = "{[)]}"
    pila = []
    diz = {"{":"}", "[":"]", "(":")"}
    errore = False
    for i, car in enumerate(stringa):
        if car in parentesi_aperte:
            push(pila, car)
        if car in parentesi_chiuse:
            parentesi = pop(pila)
            if parentesi != None:
                if diz[parentesi] != car:
                    pos_errore = i
                    errore = True
                    break
    if errore:
        print(f"errore! in posizione {pos_errore}")
    else:
        print("nessun errore!")

if __name__ == "__main__":
    main()