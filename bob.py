import random, turtle

SPOSTAMENTO = 10

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    percorso = {0: Punto(0, 0)}
    finestra = turtle.Screen()
    for tempo in range(1, 60):
        # simulare movimenti casuali
        punto_precedente = Punto(percorso[tempo - 1].x, percorso[tempo - 1].y)
        percorso[tempo] = punto_precedente
        direzione = random.choice(["nord", "sud", "est", "ovest"])
        if direzione == "nord":
            percorso[tempo].y = percorso[tempo - 1].y - SPOSTAMENTO
        elif direzione == "sud":            
            percorso[tempo].y = percorso[tempo - 1].y + SPOSTAMENTO
        elif direzione == "est":
            percorso[tempo].x = percorso[tempo - 1].x + SPOSTAMENTO
        else:
            percorso[tempo].x = percorso[tempo - 1].x - SPOSTAMENTO
        
        turt = turtle.Turtle()
        turt.goto(percorso[tempo].x, percorso[tempo].y)
        # disegnare percorso con turtle
        # BONUS controllo passaggio punto già visitato
        pass
    #scrittura su file del percorso
    #colonne: minuto, x, y
    with open("bobpath.csv", "w") as file:
        #ciclo sul dizionario
        for minuto in percorso:
            posx = percorso[minuto].x

if __name__ == "__main__":
    main()