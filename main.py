import pygame
import random
from animal import Animal, Preditor, Prey

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

    def __init__(self, win, width, height, rows):
        self.win = win
        self.width = width
        self.height = height
        self.rows = rows
        self.gap_w = self.width // self.rows
        self.gap_h = self.height // self.rows
        self.pred_cnt = 0
        self.prey_cnt = 0

        # the below (self.grid) creates the "island" and sets each tile to 0
        # these will be set to correspond to grass, water, etc... by the 
        # create_landscape function
        self.grid = [[0 for i in range(self.rows)] for j in range(self.rows)]
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
            for j in range(self.rows):
                square = Square(i, j, self.gap_w, self.gap_h, self.grid[i][j])
                self.tiles.append(square)


    def draw_island(self, animals):
        # set the background colour of the window
        self.win.fill(ORANGE)

        for tile in self.tiles:
                tile.draw(self.win)

        for i in range(self.rows):
            pygame.draw.line(self.win, GREY, 
                             (0, i * self.gap_h), 
                             (self.width, i * self.gap_h))
        for j in range(self.rows):
            pygame.draw.line(self.win, GREY, 
                             (j * self.gap_w, 0), 
                             (j * self.gap_w, self.height))
            
        for a in animals:
            if a.type == 3:
                for t in self.tiles:
                    if t.x == a.x and t.y == a.y:
                        if t.type > a.type:
                            a.alive = False
                            pygame.draw.ellipse(self.win, BLACK, 
                                                (a.x, a.y, self.gap_w, 
                                                    self.gap_h))
                        else:
                            pygame.draw.ellipse(self.win, PURPLE, 
                                                (a.x, a.y, self.gap_w, 
                                                    self.gap_h))
            elif a.type == 5:
                for t in self.tiles:
                    if t.x == a.x and t.y == a.y:
                        if t.type > a.type:
                            a.alive = False
                            pygame.draw.ellipse(self.win, WHITE, 
                                                (a.x, a.y, self.gap_w, 
                                                    self.gap_h))
                        else:
                            pygame.draw.ellipse(self.win, RED, 
                                                (a.x, a.y, self.gap_w, 
                                                    self.gap_h))
            
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

    def draw(self, win):
        if self.type == 1:
            self.make_grass()
        elif self.type == 2:
            self.make_sand()
        elif self.type == 4:
            self.make_water()
        elif self.type == 6:
            self.make_rock()

        pygame.draw.rect(win, self.color, 
                         (self.x, self.y, self.width, self.height))


def get_pos(rows, gap_w, gap_h):
    num1 = random.randint(0, rows - 1)
    num2 = random.randint(0, rows - 1)
    x = num1 * gap_w
    y = num2 * gap_h

    return x, y


def get_chk(lst, x, y):
    for i in lst:
        if i[0] == x and i[1] == y:
            chk = True
            break
        else:
            chk = False

    return chk


def main(win, width, height, start_prey, start_pred):
    ''' main is called to start the program '''
    ROWS = 10
    positions = []
    PREY = []
    PREDITORS = []
    ANIMALS = []
    chk = True

    # create the "island" where the simulator will run
    island = Island(win, width, height, ROWS)
    island.make_grid()
    
    # create the animals that will live on the island
    # 1. get the random positions for the animals to start
    for i in range(start_prey + start_pred):
        if i == 0:
            x, y = get_pos(ROWS, island.gap_w, island.gap_h)
            positions.append((x, y))
        else:
            while chk:
                x, y = get_pos(ROWS, island.gap_w, island.gap_h)
                chk = get_chk(positions, x, y)

            positions.append((x, y))
            chk = True

    # 2. create the animal using the positions
    if start_pred + start_prey == len(positions):
        cnt_prey = 0
        cnt_pred = 0
        while len(positions) > 0:
            if cnt_prey < start_prey:
                num = random.randint(0, len(positions) - 1)
                position_x = positions[num][0]
                position_y = positions[num][1]
                PREY.append(Prey(island, position_x, position_y, cnt_prey))
                cnt_prey += 1
                positions.pop(num)
            else:
                num = random.randint(0, len(positions) - 1)
                position_x = positions[num][0]
                position_y = positions[num][1]
                PREDITORS.append(Preditor(island, position_x, position_y, cnt_pred))
                cnt_pred += 1
                positions.pop(num)

            ANIMALS = PREY + PREDITORS

    run = True
    while run:
        for i in ANIMALS:
            i.reset_moved_flag()

        island.draw_island(ANIMALS)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in ANIMALS:
                    i.move_animal()
                
            if event.type == pygame.QUIT:
                run = False

        

    pygame.quit()


if __name__ == '__main__':
    main(WIN, WIDTH, HEIGHT, 5, 2)
