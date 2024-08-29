import pygame
from pygame.locals import *
import sys, random, csv

def calc_pav():
    with open("pavimento.csv", "r") as f:
        mat = [[int(c) for c in riga.split(",")] for riga in f.readlines()]
    return mat
"""{0: 0, 1: 1, 2: 3, 3: 3, 4: 2, 5: 1, 6: 2}
0,1,0,0,0,1,2
1,0,2,3,3,1,0
0,2,0,2,1,0,0
0,3,2,0,0,0,1
0,3,1,0,0,1,0
1,1,0,0,1,0,0
2,0,0,1,0,0,0
"""
def scelta_nodo(non_visitati, label):
    min_label = sys.maxsize
    min_nodo = None
    for nodo in non_visitati:
        label_nodo = label[nodo]
        if label_nodo < min_label:
            min_label = label_nodo
            min_nodo = nodo
    return min_nodo

def percorso(precedenti):
    dest = 4
    sorgente = 0
    lista = [dest]
    prec = precedenti[dest]
    lista.append(prec)
    while precedenti != sorgente:
        precedenti = prec[precedenti]
        lista.append(precedenti)
    lista = lista[::-1]
    return lista

def algoritmoDijstrak2(nodo_sorgente, matrice):
    
    n_nodi = len(matrice)

    non_visitati = set([i for i in range(0, n_nodi)])
    label = {i: sys.maxsize for i in range(0, n_nodi)}
    precedenti = {i: None for i in range(n_nodi)}
    label[nodo_sorgente] = 0
    
    while len(non_visitati) > 0:
        nodoCorrente = scelta_nodo(non_visitati, label)
        print(non_visitati)
        non_visitati.remove(nodoCorrente)

        for nodo_vicino, peso in enumerate(matrice[nodoCorrente]):
            if peso > 0:
                nuova_label = label[nodoCorrente] + peso
                if nuova_label < label[nodo_vicino]:
                    precedenti[nodo_vicino] = nodoCorrente
                    label[nodo_vicino] = nuova_label
        
    
    return label, precedenti

def generate_maze(width, height):
    maze = [[0 for _ in range(width)] for _ in range(height)]

    # Initialize walls as borders
    for i in range(width):
        maze[0][i] = -1
        maze[height - 1][i] = -1
    for i in range(height):
        maze[i][0] = -1
        maze[i][width - 1] = -1

    # Recursive backtracking to create paths
    stack = [(1, 1)]
    while stack:
        x, y = stack[-1]
        neighbors = [(x-2, y), (x+2, y), (x, y-2), (x, y+2)]
        unvisited_neighbors = [(nx, ny) for nx, ny in neighbors if 0 < nx < width-1 and 0 < ny < height-1 and maze[ny][nx] == 0]

        if unvisited_neighbors:
            nx, ny = random.choice(unvisited_neighbors)
            maze[ny][nx] = 1
            maze[(ny+y)//2][(nx+x)//2] = 1
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

def save_maze_to_csv(maze, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in maze:
            writer.writerow(row)

def main():

    lato_x = 100
    lato_y = 100
    pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    matrice =  [[0,1,0,0,0,1,2],
                [1,0,2,3,3,1,0],
                [0,2,0,2,1,0,0],
                [0,3,2,0,0,0,1],
                [0,3,1,0,0,1,0],
                [1,1,0,0,1,0,0],
                [2,0,0,1,0,0,0]]
    k = 1
    a, b = algoritmoDijstrak2(0,matrice)
    print(a)
    d_ad = {i: [j for j, n in enumerate(matrice[i]) if n] for i in range(len(matrice))}
    num_celle_libere = max(d_ad.keys())
    print(d_ad)
    matrice_pesi = [[0]*num_celle_libere for _ in range(num_celle_libere)]
    for i in range(num_celle_libere):
        for j in range(num_celle_libere):
            if j+1 in d_ad[i+1]:
                matrice_pesi[i][j] = 1

    pygame.init()
    screen = pygame.display.set_mode((n_x * lato_x , n_y * lato_y))
    muro = pygame.image.load("muro.jpg")
    strada = pygame.image.load("pavimento.webp")
    robot = pygame.image.load("robot.png").convert_alpha()
    font = pygame.font.SysFont("Verdana", 18) 
    
    for riga in pavimento:
        for casella in riga:
            surf1 = pygame.Surface((lato_x, lato_y))
            text = font.render(f"{k}", True, (0,0,0))
            if casella == -1:
                surf1.blit(muro, (0, 0))
                screen.blit(surf1, (lato_x-100, lato_y-100))  
            if casella == 0:
                surf1.blit(strada, (0, 0))
                text_pos = text.get_rect(center=(lato_x-20, lato_y-80))  
                screen.blit(surf1, (lato_x-100, lato_y-100))  
                screen.blit(text, text_pos)
                k += 1
            if casella == 2:
                surf1.blit(strada, (0, 0))
                text_pos = text.get_rect(center=(lato_x-20, lato_y-80))  
                screen.blit(surf1, (lato_x-100, lato_y-100))
                screen.blit(robot, (lato_x-100, lato_y-100)) 
                screen.blit(text, text_pos)
                k += 1
            
            pygame.display.flip()
            lato_x += 100
            
        lato_x = 100
        lato_y += 100

        #screen.blit(robot, (0, 0))
    k = 1
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0 or casella == 2:
                matrice[indice_riga][indice_colonna] = k
                k += 1
    
    diz = {}
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            adiacenze = []
            if casella > -1:
                if indice_riga > 0:
                    if matrice[indice_riga-1][indice_colonna] != -1:
                        adiacenze.append(matrice[indice_riga-1][indice_colonna])
                if indice_colonna > 0:
                    if matrice[indice_riga][indice_colonna-1] != -1:
                        adiacenze.append(matrice[indice_riga][indice_colonna-1])
                if indice_riga < n_y-1:
                    if matrice[indice_riga + 1][indice_colonna] != -1:
                        adiacenze.append(matrice[indice_riga+1][indice_colonna])
                if indice_colonna < n_x - 1:
                    if matrice[indice_riga][indice_colonna + 1] != -1:
                        adiacenze.append(matrice[indice_riga][indice_colonna+1])
                    diz[matrice[indice_riga][indice_colonna]] = adiacenze                    


                



    #pygame.quit()
    #exit()
    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
    pygame.quit()


if __name__ == "__main__":
    main()