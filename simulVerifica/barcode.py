"""Un codice a barre è definito da una sequenza di barre nere oppure bianche secondo questi requisiti:
le barre nere corrispondono a un’1 e le barre bianche corrispondono a uno 0;
le barre sono disegnate su sfondo bianco;
una barra nera è rappresentata mediante una linea nera spessa 4 pixel e lunga 100 pixel;
una barra bianca è rappresentata mediante una linea bianca spessa 4 pixel e lunga 100 pixel;
barre adiacenti sono separate tra loro da uno spessore di un pixel;
un codice a barre è composto in totale da 64 barre.
Il codice a barre è utilizzato per codificare stringhe alfanumeriche di 8 caratteri.
Ogni carattere della stringa alfanumerica è convertito nel suo codice ASCII 
(vedi funzione ord()) e successivamente nella sua rappresentazione binaria, 
quindi nel complesso 8 caratteri corrispondono a 64 bit totali. Non devono 
essere presenti caratteri che hanno codice ASCII maggiore di 255.
Crea un programma in linguaggio Python 3 nel quale:
sia presente una classe Barcode che implementi il codice a barre sopra descritto;
la classe abbia un metodo che disegni il codice a barre a partire dalla stringa 
alfanumerica di 8 caratteri, utilizzando il modulo turtle;
sia presente una funzione main() che testi la classe."""

import turtle


class Barcode():
    def __init__(self, nome):
        self.LUNG = 64*4
        self.ALT = 100
        self.SEP = 1
        self.nome = nome
        nomeInBin = ""
        if len(self.nome) < 8:
            nUnderscore = "_" * (8 - len(self.nome))
            self.nome = f"{self.nome}{nUnderscore}"
        elif len(self.nome) > 8:
            self.nome = self.nome[:8]
        self.nomeInAscii = [bin(ord(char)) for char in self.nome]
        self.nomeInAscii = [string.replace("0b", "") for string in self.nomeInAscii]
        for string in self.nomeInAscii:
            if len(string) < 8:
                nZeri = "0" * (8 - len(string))
            nomeInBin += f"{nZeri}{string}"
        self.nomeInAscii = nomeInBin
        

    def disegnaBarra(self, omar, num):
        if num == 0:
            omar.color("white")
            for i in range(2):
                omar.forward(self.LUNG)
                omar.left(90)
                omar.forward(self.ALT)
                omar.left(90)
        else:
            omar.color("black")
            omar.begin_fill()
            for i in range(2):
                omar.forward(self.LUNG)
                omar.left(90)
                omar.forward(self.ALT)
                omar.left(90)
            omar.end_fill()
        omar.penup()
        omar.forward(self.LUNG + self.SEP)
        omar.pendown()

    def disegnaCodice(self, barcode):
        finestra = turtle.Screen() 
        omar = turtle.Turtle()
        listaBarcode = [char for char in barcode]
        for i in range(64):
            self.disegnaBarra(omar, int(listaBarcode[i]))

        finestra.mainloop()

def main():
    codiceBarre = Barcode("ciao")
    
    codiceBarre.disegnaCodice(codiceBarre.nomeInAscii)


if __name__ == "__main__":
    main()
