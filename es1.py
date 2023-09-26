def main():#defininizione della funzione main
    nome = input("come ti chiami?")
    anni = int(input("quanti anni hai?"))
    anno_corrente = int(input("in quale anno siamo?"))


    print(f"ti chiami {nome} e hai {anni} anni")
    print(f"sei nato nel {anno_corrente - anni}")
    #print(type(anni))   #type stampa il tipo di variabile

if __name__=="__main__":
    main()