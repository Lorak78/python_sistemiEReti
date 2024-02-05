def main():
    #tuples 
    #le tuple sono (a differenza della lista) immutabili
    #non si può assegnare ad un elemento di una tupla
    t = (3, 4, 5, 6)
    #t[1] = 9   ERRORE
    print(t[0])

    punto = (3, 4)
    x, y = punto #assegnazione multipla, spacchettamento tupla
    print(t)
    print(y)

if __name__ == "__main__":
    main()