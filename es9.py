#chiedere un numero n tra 1 e 31 che rappresenta una subnet in cidr
#scrivere la subnet in notazione decimale puntata
def main():
    nUno = int(input("inserisci la subnet in cidr: "))
    nZero = 31 - nUno
    strUno = "1" * nUno
    strZero = "0" * nZero
    print(f"{strUno} {strZero}")
    strSubnetBin = strUno + strZero
    group1 = int(strSubnetBin[0:8], 2)
    group2 = int(strSubnetBin[8:16], 2)
    group3 = int(strSubnetBin[16:24], 2)
    group4 = int(strSubnetBin[24:32], 2)
    print(f"{group1}.{group2}.{group3}.{group4}")


if __name__ == "__main__":
    main()