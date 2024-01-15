import math
def main():
    d = {}
    n1 = int(input("inserisci il primo numero: "))
    n2 = int(input("inserisci il secondo numero: "))
    mediaAritmetica = (n1 + n2) / 2
    d[mediaAritmetica] = "media aritmetica"
    mediaGeometrica = math.sqrt(n1 * n2)
    d[mediaGeometrica] = "media geometrica"
    print(d)

if __name__ == "__main__":
    main()