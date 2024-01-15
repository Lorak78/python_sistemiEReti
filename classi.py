class Quadrato():  #WOAH classi in python!!!
    def __init__(self, lato):#self è il parente di this in java
        self.lato = lato
    def calcolaArea(self):
        return self.lato**2
    def stampaLato(self):
        print(f"il lato è lungo: {self.lato}")

def main():
    q = Quadrato(4)
    print(f"l'area del quadrato q è {q.calcolaArea()}")
    print(q.lato)


if __name__ == "__main__":
    main()