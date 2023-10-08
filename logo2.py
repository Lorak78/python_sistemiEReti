#chiedi un numero n intero e con turtle disegni poligono regolare n lati
import turtle #esempio di importazione modulo built-in/nativo

finestra = turtle.Screen() #creazione finestra
omar = turtle.Turtle() #creazione tartaruga

n = int(input("inserisci il numero di lati: "))
lungLato = int(input("inserisci la lunghezza del lato: "))
omar.color("cyan")

omar.fillcolor("cyan")
omar.begin_fill()

for i in range(0, n):
    omar.forward(lungLato)
    omar.left(360 / n)
    
omar.end_fill()



finestra.mainloop() #