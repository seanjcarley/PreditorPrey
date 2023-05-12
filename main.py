import pygame
import random
from animal import Animal

pygame.font.init()  # initialise the font

WIDTH, HEIGHT = 800, 600  # window size
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # create the pygame window
pygame.display.set_caption('Preditor-Prey Simulator')  # set the title
MAIN_FONT = pygame.font.SysFont('comicsans', 40)  # set the font style and size
FPS = 1  # set the frame per second limit

# Colours (R, G, B)
BLACK = (0, 0, 0)
GREY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 127, 0)
LIME = (127, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)


class Island:
    ''' island class used to create game area and set tile types '''

    def __init__(self, win, width, height, prey_cnt, pred_cnt, rows):
        self.win = win
        self.width = width
        self.height = height
        self.rows = rows
        self.gap_w = self.width // self.rows
        self.gap_h = self.height // self.rows

        # the below (self.grid) creates the "island" and sets each tile to 0
        # these will be set to correspond to grass, water, etc... by the 
        # create_landscape function
        self.grid = [[0 for i in range(self.rows)] for j in range(self.rows)]
        
        self.prey_cnt = prey_cnt
        self.pred_cnt = pred_cnt
        self.tiles = []


    def create_landscape(self):
        ''' set the tile type (i.e. grass, water, etc...) '''
        for i in self.grid:
            for j in range(len(i)):
                choice = random.randint(1, 15)
                if choice == 4:
                    t = 6  # rock
                elif choice == 5 or choice == 6:
                    t = 4  # water
                elif choice == 15:
                    t = 2  # sand
                else:
                    t = 1  # grass
                i[j] = t


    def make_grid(self):
        self.create_landscape()

        for i in range(self.rows):
            self.tiles.append([])
            for j in range(self.rows):
                square = Square(i, j, self.gap_w, self.gap_h, self.grid[i][j])
                self.tiles[i].append(square)

    
    def make_animals(self, tile):
        tile.draw(self.win)
        pygame.display.update()
        


    def draw_island(self):
        # set the background colour of the window
        self.win.fill(ORANGE)

        for row in self.tiles:
            for tile in row:
                tile.draw(self.win)

        for i in range(self.rows):
            pygame.draw.line(self.win, GREY, 
                             (0, i * self.gap_h), 
                             (self.width, i * self.gap_h))
        for j in range(self.rows):
            pygame.draw.line(self.win, GREY, 
                             (j * self.gap_w, 0), 
                             (j * self.gap_w, self.height))
        
        pygame.display.update()


class Square:
    ''' square class to create tiles for the game area and hold 
        the attributes 
    '''
    def __init__(self, row, col, width, height, type):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * height
        self.width = width
        self.height = height
        self.type = type
        self.color = BLACK

    
    def get_pos(self):
        return self.row, self.col

    
    def make_grass(self):
        self.color = GREEN

    
    def make_water(self):
        self.color = BLUE


    def make_rock(self):
        self.color = GREY


    def make_sand(self):
        self.color = YELLOW

    
    def make_animal(self):
        self.color = CYAN


    def make_prey(self):
        self.color = PURPLE

    
    def make_pred(self):
        self.color = RED

    def draw(self, win):
        if self.type == 1:
            self.make_grass()
        if self.type == 2:
            self.make_sand()
        if self.type == 3:
            self.make_prey
        if self.type == 4:
            self.make_water()
        if self.type == 5:
            self.make_pred
        if self.type == 6:
            self.make_rock()
        if self.type == 7:
            self.make_animal()

        pygame.draw.rect(win, self.color, 
                         (self.x, self.y, self.width, self.height))


def get_pos(rows, gap_w, gap_h):
    num1 = random.randint(0, rows - 1)
    num2 = random.randint(0, rows - 1)
    x = num1 * gap_w
    y = num2 * gap_h

    return x, y


def get_chk(animals, x, y):
    for a in animals:
        if x == a.x and y == a.y:
            chk = True
            break
        else:
            chk = False

    return chk


def main(win, width, height, start_prey, start_pred):
    ''' main is called to start the program '''
    ROWS = 5
    ANIMALS = []
    chk = True

    # create the "island" where the simulator will run
    island = Island(win, width, height, start_prey, start_pred, ROWS)
    island.make_grid()
    
    # Create the Animals that will live on the island and set 
    # their start position
    for i in range(start_pred):
        if len(ANIMALS) == 0:
            x, y = get_pos(ROWS, island.gap_w, island.gap_h)
            ANIMALS.append(Animal(island, x, y, f'Animal_{i}'))
        else:
            while chk:
                x, y = get_pos(ROWS, island.gap_w, island.gap_h)
                chk = get_chk(ANIMALS, x, y)
            
            ANIMALS.append(Animal(island, x, y, f'Animal_{i}'))
            chk = True
                    
    for a in ANIMALS:
        print(f'{a.name} is at position {(a.x, a.y)}, and it\'s moved flag is set at {a.moved}')
        x, y = a.x, a.y
        for j in island.tiles:
            for k in j:
                if a.x == k.x and a.y == k.y:
                    k.type = a.type
                    island.make_animals(k)


    run = True
    while run:
        island.draw_island()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main(WIN, WIDTH, HEIGHT, 5, 2)
