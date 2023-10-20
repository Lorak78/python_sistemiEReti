def main():
    stringa = "ciao"
    for indice in range(len(stringa)):
        if indice % 2 != 0:
            print(stringa[indice], end = "")

if __name__ == "__main__":
    main()