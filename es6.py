def main():
    num = int(input("inserisci un numero: "))
    if num % 3 != 0:
        print("numero non divisibile per 3")
    else:
        print("numero divisibile per 3")

if __name__ == "__main__":
    main()