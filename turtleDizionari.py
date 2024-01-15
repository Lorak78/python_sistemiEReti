import turtle
def nord(t, nPixel):
    t.seth(90)
    t.forward(nPixel)
    
def sud(t, nPixel):
    t.seth(270)
    t.forward(nPixel)
    
def est(t, nPixel):
    t.seth(0)
    t.forward(nPixel)
    
def ovest(t, nPixel):
    t.seth(180)
    t.forward(nPixel)
    

def main():
    finestra = turtle.Screen() #creazione finestra
    NPIXEL = 100
    cicla = True
    t = turtle.Turtle() #creazione tartaruga
    movimenti = {"nord":nord, "sud":sud, "est":est, "ovest":ovest}
    while cicla:
        direzione = input("inserisci la direzione tra nord, sud, est e ovest, qualsiasi altra cosa per uscire")
        if direzione in movimenti:
            movimenti[direzione](t, NPIXEL)
        else:
            if input("vuoi uscire?") == "si":
                cicla = False

    finestra.mainloop()
if __name__ == "__main__":
    main()