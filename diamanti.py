#chiedere num n dispari
#stampare nel terminale un diamante di asterischi

def main():
    n = 0
    while n % 2 == 0:
        n = int(input("inserisci un numero dispari"))
    spazi = n // 2
    for i in range(1, n + 1, 2):
        print(" " * spazi + "*" * i)
        spazi -= 1
    spazi = 1
    for i in range(n - 2, 0, -2):
        print(" " * spazi + "*" * i)
        spazi += 1
        

if __name__ == "__main__":
    main()