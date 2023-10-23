def main():
    tavPitagorica = [[k * i for i in range(1, 11)] for k in range(1, 11)]
    for k, tabellina in enumerate(tavPitagorica):
        #tabellina e' una lista
        #power e' una lista di liste
        #enumerate e' una funzione che numera le liste e restituisce indice e elemento
        #evitare contatori -> quando esistono i contatori uso enumerato
        print(f"tabellina del {k + 1}: {tabellina}")
    file = open("tavPitagorica.txt", "w")
    for tabellina in tavPitagorica:
        file.write(f"{tabellina}\n")
        
        file.close()



if __name__ == "__main__":
    main()