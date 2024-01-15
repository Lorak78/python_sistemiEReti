#chiedere num n dispari
#stampare nel terminale un diamante di asterischi

def main():
    n = int(input("inserisci un numero dispari"))
    spazi = int(n / 2)
    for i in range(1, n + 1, 2):
        print(" " * spazi + "*" * i)
        spazi -= 1
    spazi += 1
    for i in range(n - 2, 0, -2):
        spazi += 1
        print(" " * spazi + "*" * i)
        

if __name__ == "__main__":
    main()