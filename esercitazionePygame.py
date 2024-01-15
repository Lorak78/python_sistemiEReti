import pygame, random

BOB_SIZE = (5, 5)
DIS = 10
HOME_SIZE = (50, 50)
WIN_RESOLUTION = (640, 480)
HOME_POS = [(50, 50), (590, 50), (50, 420), (590, 420)]
FPS = 60
WIN_CENTER = (WIN_RESOLUTION[0] / 2, WIN_RESOLUTION[1] / 2)
NUM_DIRS = 4

class Bob():
    def __init__(self):
        self.surf = pygame.Surface(BOB_SIZE)
        self.rect = self.surf.get_rect()
        self.surf.fill("white")
        self.rect.center = WIN_CENTER
        self.MOVEMENT = [self.north, self.south, self.east, self.west]
        self.distance_traveled = {}

    def north(self):
        self.rect.y -= DIS

    def south(self):
        self.rect.y += DIS

    def east(self):
        self.rect.x -= DIS

    def west(self):
        self.rect.x += DIS

    def move_random(self):
        self.MOVEMENT[random.randint(0, NUM_DIRS - 1)]()

class Home():
    def __init__(self):
        self.surf = pygame.Surface(HOME_SIZE)
        self.rect = self.surf.get_rect()
        self.surf.fill("yellow")
        self.rect.center = random.choice(HOME_POS)

def main():
    pygame.init()
    pygame.display.set_caption("bob")
    screen = pygame.display.set_mode(WIN_RESOLUTION)
    clock = pygame.time.Clock()
    bob = Bob()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        bob.move_random()
        with open("bobpath.csv", "a") as file:
            file.write(f"{bob.rect.center}\n")

        screen.blit(bob.surf, bob.rect)
        pygame.display.update()
        clock.tick(FPS)
     
     
if __name__=="__main__":
    main()