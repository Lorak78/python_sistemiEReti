class Quadrato():
    def __init__(self, lato):
        self.lato = lato

    def calcolaArea(self):
        return self.lato**2
    
    def calcolaPerimetro(self):
        return self.lato * 4
    
    def puntoEsterno(self, x, y):
        return (x > 0 and x < self.lato and y > 0 and y < self.lato)
    
    def stampaLato(self):
        print(f"il lato è lungo: {self.lato}")
    


def main():
    q = Quadrato(5)
    esterno = q.puntoEsterno(6, 6)
    print(esterno)
    pass

if __name__ == "__main__":
    main()