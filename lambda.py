#Lambda function: utile per definire funzioni brevi

#lambda:
somma = lambda x, y: x + y 
def main():
    x = [10, 4]
    print(somma(*x)) #spacchettamento della lista sui parametri
    #funziona solo se len(x) == num parametri

if __name__ == "__main__":
    main()