#chiedi in input un numero n e stampi una stella di n punti

import turtle

finestra = turtle.Screen()
omar = turtle.Turtle()
n = int(input("inserisci il numero di punti di una stella: "))
omar.color("red")#colore della linea (cursore)
omar.speed("slow")#velocità turtle
gradi = 720 / n

for i in range(n):
    omar.forward(150)
    omar.right(gradi)

finestra.mainloop()
