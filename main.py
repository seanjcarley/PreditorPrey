import pygame
import random
from animal import Preditor, Prey

pygame.font.init()  # initialise the font

WIDTH, HEIGHT = 800, 600  # window size
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # create the pygame window
pygame.display.set_caption('Preditor-Prey Simulator')  # set the title
MAIN_FONT = pygame.font.SysFont('comicsans', 20)  # set the font style and size
FPS = 2  # set the frame per second limit
MAX_MOVES = 100
MAX_ISLAND_AGE = 150
STARTING_PREY = 10
STARTING_PRED = 4

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
        self.max_moves = 300
        # the below (self.grid) creates the "island" and sets each tile to 0
        # these will be set to correspond to grass, water, etc... by the 
        # create_landscape function
        self.grid = [[0 for i in range(self.rows)] for j in range(self.rows)]
        self.tiles = []
        self.prey = []  # keep track of prey that are still alive
        self.pred = []  # keep track of preditors that are still alive
        self.dead_prey = []  # keep track of prey that have died
        self.dead_pred = []  # keep track of preditors that have died
        self.island_age = 0


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


    def draw_island(self):
        # set the background colour of the window
        self.win.fill(ORANGE)

        prey_txt = MAIN_FONT.render(f'Prey Population: {len(self.prey)}', 1, WHITE)
        pred_txt = MAIN_FONT.render(f'Preditor Population: {len(self.pred)}', 1, WHITE)
        move_txt = MAIN_FONT.render(f'Total Moves: {self.island_age}', 1 , WHITE)

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
            
        for prey in self.prey:
            for t in self.tiles:
                if t.x == prey.x and t.y == prey.y:
                    if t.type > prey.type:
                        prey.died()
                    else:
                        pygame.draw.ellipse(self.win, PURPLE, 
                                            (prey.x, prey.y, self.gap_w, 
                                                self.gap_h))
        
        for pred in self.pred:
            for t in self.tiles:
                if t.x == pred.x and t.y == pred.y:
                    if t.type > pred.type:
                        pred.died()
                    else:
                        pygame.draw.ellipse(self.win, RED, 
                                            (pred.x, pred.y, self.gap_w, 
                                                self.gap_h))
                        
        self.win.blit(prey_txt, (20, 20))
        self.win.blit(pred_txt, (20, 20 + prey_txt.get_height()))
        self.win.blit(move_txt, (self.width - move_txt.get_width() - 20, 20))
            
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
    ROWS = 25
    positions = []
    ANIMALS = []
    chk = True
    clock = pygame.time.Clock()

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
                island.prey.append(Prey(island, position_x, position_y, cnt_prey))
                cnt_prey += 1
                positions.pop(num)
            else:
                num = random.randint(0, len(positions) - 1)
                position_x = positions[num][0]
                position_y = positions[num][1]
                island.pred.append(Preditor(island, position_x, position_y, cnt_pred))
                cnt_pred += 1
                positions.pop(num)

    run = True
    while run:
        island.island_age += 1
        ANIMALS = island.prey + island.pred
        clock.tick(FPS)
        for i in ANIMALS:
            i.reset_moved_flag()

        island.draw_island()

        for event in pygame.event.get():
            # can be used to progress the simulation by clicking the mouse
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     for a in ANIMALS:
            #         if a.age < 10:
            #             a.move_animal()
            #         else:
            #             a.died()
                
            if event.type == pygame.QUIT:
                run = False

        for a in ANIMALS:
            if a.age < MAX_MOVES:
                a.move_animal()
            else:
                a.died()

    pygame.quit()


if __name__ == '__main__':
    main(WIN, WIDTH, HEIGHT, STARTING_PREY, STARTING_PRED)
