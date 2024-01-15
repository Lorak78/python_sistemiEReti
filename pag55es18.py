def popolaLista(l):
    n1 = int(input("inserisci il primo numero: "))
    n2 = int(input("inserisci il secondo numero: "))
    l.append(n1**2 + n2**2)
    l.append((n1 + n2) ** 2)
    l.append(n1**2 - n2**2)
    l.append((n1 - n2) ** 2)

def main():
    lista = []
    popolaLista(lista)
    print(lista)
    

if __name__ == "__main__":
    main()