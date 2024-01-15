import random

class Nemico():
    def __init__(self, posx, posy, nVite):
        self.posx = posx
        self.posy = posy
        self.nVite = nVite
    def stampa(self):
        print(f"nemico in posizione: {self.posx},{self.posy} con {self.nVite} vite")

def main():
    N_NEMICI = 5
    HEIGHT = 400
    WIDTH = 800
    lista_nemici = []
    for i in range(N_NEMICI):
        nemico = Nemico(random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1), 5)
        lista_nemici.append(nemico)

    print(lista_nemici)
    personaggio = {"posx": 100, "posy":200}
    for nemico in lista_nemici:
        nemico.stampa()
    if nemico.posx == personaggio["posx"] and nemico.posy == personaggio["posy"]:
        print("collisione") 

if __name__ == "__main__":
    main()