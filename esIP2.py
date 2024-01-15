#chiedere un numero n tra 1 e 31 che rappresenta una subnet in cidr
#scrivere la subnet in notazione decimale puntata
def ipBinToDec(ipBin):
    gruppiDec = []
    for i in range(0, 32, 8):
        ottetto = ipBin[i:i+8]
        gruppiDec.append(str(int(ottetto, 2)))
    return ".".join(gruppiDec)

def main():
    ipBinario = input("Inserisci l'ip in binario")
    ipDec = ipBinToDec(ipBinario)
    print(ipDec)


if __name__ == "__main__":
    main()