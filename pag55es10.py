#con input da tastiera
def main():
    lista_voti = []
    k = 0
    while True:
        voto = int(input("inserisci un voto. (-1 per interrompere)"))
        if voto < 0 and k >= 6:
            break
        lista_voti.append(voto)
        k += 1
    print(lista_voti[1:-1])
    lista_voti[3] = 10
    print(lista_voti[0:3])

def main1():
    lista_voti = [5, 9, 8, 7.5, 6, 8]
    print(lista_voti[1:-1])
    lista_voti[3] = 10
    print(lista_voti[0:3])

if __name__ == "__main__":
    main()