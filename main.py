import pygame
import random
from animal import Preditor, Prey
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Preditor-Prey Simulator')
MAIN_FONT = pygame.font.SysFont('comicsans', 40)
FPS = 10

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


class Square:
    def __init__(self, row, col, width, total_rows, type):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.type = type

        if self.type == "rock":
            self.color = GREY
        if self.type == "water":
            self.color = BLUE
        if self.type == "grass":
            self.color = GREEN
        if self.type == "sand":
            self.color = YELLOW
        

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))


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


def draw(win, grid, rows, width):
    win.fill(GREY)

    for row in grid:
        for square in row:
            square.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            choice = random.randint(1, 15)
            if choice == 4:
                sq_type = "rock"
            elif choice == 5 or choice == 6:
                sq_type = "water"
            elif choice == 15:
                sq_type = "sand"
            else:
                sq_type = "grass"
            square = Square(i, j, gap, rows, sq_type)
            grid[i].append(square)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main(WIN, WIDTH)