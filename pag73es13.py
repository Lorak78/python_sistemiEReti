class Robot():
    def __init__(self, nome, massa, tipologia):
        self.nome = nome
        if massa > 0:
            self.massa = massa
        else:
            self.massa = 60
        self.tipologia = tipologia
    def pericoloso(self):
        return (self.massa >= 100 and self.tipologia == "umanoide")


def main():
    r = Robot("tom", 132, "umanoide")
    robot = r.pericoloso()
    print(robot)
    pass

if __name__ == "__main__":
    main()