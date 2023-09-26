def main():
    num = int(input("inserisci un numero: "))
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        print("numero divisibile per 2, per 3 o per 5")
    else:
        print("numero non divisibile per 2, per 3 o per 5")
    

if __name__ == "__main__":
    main()