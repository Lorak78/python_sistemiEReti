"""
turtle che può eseguire 
forward(100) che chiamo "F"
right(90) che chiamo "R"
left(90) che chiamo "L"
chiedere all'utente il comando da dare (blocca con -1):
salvare i comandi in una lista
"""

import turtle

def main():
    listaComandi = []
    comandiPossibili = ["F", "R", "L"]
    comando = "F"
    finestra = turtle.Screen() #creazione finestra
    omar = turtle.Turtle() #creazione tartaruga
    while comando in comandiPossibili:
        comando = input(f"inserisci il comando tra questi: {comandiPossibili}")
        if comando == "F" or comando == "R" or comando == "L":
            listaComandi.append(comando)
    for comando in listaComandi:
        if comando == "F":
            omar.forward(100)
        if comando == "L":
            omar.left(90)
        if comando == "R":
            omar.left(90)
    finestra.mainloop()        
    

if __name__ == "__main__":
    main()