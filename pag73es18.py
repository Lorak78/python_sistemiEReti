import math
def main():
    #soluzione ottimale: listaQuadratiPerf = [num**2 for num in range(int(math.sqrt(200) + 1)) if num % 2 != 0]
    lista = [num**2 for num in range(int(math.sqrt(200) + 1)) if num % 2 != 0 and (i**2 < 200)]
    print(lista)

def main1():
    listaQuadratiPerf = [num**2 for num in range(int(math.sqrt(200) + 1)) if num % 2 != 0]
    print(listaQuadratiPerf)

def main2():
    listaQuadratiPerf = [num**2 for num in range(200) if num % 2 != 0]
    print(listaQuadratiPerf)

if __name__ == "__main__":
    main()