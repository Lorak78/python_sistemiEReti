#Le liste

def printList(l):
    print("la lista è ", end="")
    for i in l:
        print(i, end=" ")
    print("\n")

def main():
    #l = [1, 2, 3, 4, "c", 3.14, "pythone"]
    #r = l[::-1]
    #print(l)
    #slicing di liste
    #print(l[-1])
    #print(l[::-1])
    #printList(3 * l)#concatenazione

    #vogliamo permettere all'utente di caricare 
    #una lista
    lista = []
    num = 1
    while num >= 0:
        num = int(input("scrivi un num (-1 per interrompere): "))
        if num >= 0:
            lista.append(num) #qualsiasi cosa è un oggetto: lista ha metodo append che 
                            #aggiunge un elemento a lista
    printList(lista)

if __name__ == "__main__":
    main()