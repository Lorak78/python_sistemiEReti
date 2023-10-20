#disegnare i poligoni da 3 a 11 in 1 schermata usare penup() e pendown()

import turtle

def disegnaPoligono(t, num, lato):
    #disegna poligono
    gradi = 360 / num
    t.begin_fill()
    for i in range(0, num):
        t.forward(lato)
        t.left(gradi)
    t.end_fill()


def main():
    finestra = turtle.Screen()
    omar = turtle.Turtle()

    omar.penup()#alza penna
    omar.left(135)
    omar.forward(400)
    omar.pendown()#comincia a disegnare
    omar.goto(0, 0)#la turtle si posiziona in x, y
    omar.shape("turtle")

    for i in range(3, 11):
        for j in range(3, i):
            x, y = disegnaPoligono(omar, 4, 100)
        

    finestra.mainloop()


if __name__ = "__main__":
    main()