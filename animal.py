import random

class Animal:
    ''' parent class for preditor and prey classes '''
    def __init__(self, island, x=0, y=0, name='A'):
        self.island = island
        self.x = x
        self.prev_x = 0
        self.y = y
        self.prev_y = 0
        self.prev_dir = None
        self.name = f'Animal_{name}'
        self.type = 7
        self.alive = True
        self.moved = False
        self.age = 0
        self.breed_clock = 0
        self.offspring = 0
        self.possible_moves = []

    
    def __str__(self):
        ''' return the object name '''
        return self.name
    

    def __repr__(self):
        ''' returns printable representation of specified object '''
        return self.__str__()
    

    def current_state(self):
        txt = f'Name: {self.name}\nAge: {self.age}\nLocation: ({self.x}, {self.y})'
        return txt

    
    def check_possible_moves(self):
        ''' function to check the possible available positions for the object 
        to move to'''
        # for x in range(-1, 2):
        #     for y in range(-1, 2):
        #         [self.x + (x * self.island.gap_w), \
        #                 self.y + (y * self.island.gap_h)]

        # set the available positions direction relative to the object
        move_tiles = {
            'north': [self.x, self.y - self.island.gap_h],
            'north_e': [self.x + self.island.gap_w, self.y - self.island.gap_h],
            'east': [self.x + self.island.gap_w, self.y],
            'south_e': [self.x + self.island.gap_w, self.y + self.island.gap_h],
            'south': [self.x, self.y + self.island.gap_h],
            'south_w': [self.x - self.island.gap_w, self.y + self.island.gap_h],
            'west': [self.x - self.island.gap_w, self.y],
            'north_w': [self.x - self.island.gap_w, self.y - self.island.gap_h],
        }

        # add the co-ordinates of the available position to the available 
        # position list
        for tile in self.island.tiles:
            if not tile.occupied:
                if tile.co_ords == move_tiles['north'] and self.type > tile.type:
                    self.possible_moves.append(move_tiles['north'])  # up
                elif tile.co_ords == move_tiles['north_e'] and self.type > tile.type:
                    self.possible_moves.append(move_tiles['north_e'])  # up and right
                elif tile.co_ords == move_tiles['east'] and self.type > tile.type:
                    self.possible_moves.append(move_tiles['east'])  # right
                elif tile.co_ords == move_tiles['south_e'] and self.type > tile.type:
                    self.possible_moves.append(move_tiles['south_e'])  # down and right
                elif tile.co_ords == move_tiles['south'] and self.type > tile.type:
                    self.possible_moves.append(move_tiles['south'])  # down
                elif tile.co_ords == move_tiles['south_w'] and self.type > tile.type:
                    self.possible_moves.append(move_tiles['south_w'])  # down and left
                elif tile.co_ords == move_tiles['west'] and self.type > tile.type:
                    self.possible_moves.append(move_tiles['west'])  # left
                elif tile.co_ords == move_tiles['north_w'] and self.type > tile.type:
                    self.possible_moves.append(move_tiles['north_w'])  # left and up

    
    def set_prev_dir(self, x, y):
        # function to keep track of object direction to make movement less random
        if x == 0 and y == self.island.gap_h:
            self.prev_dir = 'N'
        elif x == -self.island.gap_w and y == self.island.gap_h:
            self.prev_dir = 'NE'
        elif x == -self.island.gap_w and y == 0:
            self.prev_dir = 'E'
        elif x == -self.island.gap_w and y == -self.island.gap_h:
            self.prev_dir = 'SE'
        elif x == 0 and y == -self.island.gap_h:
            self.prev_dir = 'S'
        elif x == self.island.gap_w and y == -self.island.gap_h:
            self.prev_dir = 'SW'
        elif x == self.island.gap_w and y == 0:
            self.prev_dir = 'W'
        elif x == self.island.gap_w and y == self.island.gap_h:
            self.prev_dir = 'NW'


    def set_new_location(self, coords):
        ''' update object position '''
        self.x, self.y = coords

    
    def move_animal(self):
        ''' move the object'''
        self.check_possible_moves()
        no_of_moves = len(self.possible_moves)

        if no_of_moves > 0:
            if no_of_moves > 1:
                num = random.randint(0, no_of_moves - 1)
            elif no_of_moves == 1:
                num = 0

            x = self.x - self.possible_moves[num][0]
            y = self.y - self.possible_moves[num][1]

            if self.breed_clock > 0:
                self.breed_clock -= 1
                if self.prev_dir is None:
                    self.set_prev_dir(x, y)
                    self.set_new_location(self.possible_moves[num])
                    self.moved = True
                elif self.prev_dir == 'N':
                    move_n = [self.x, self.y - self.island.gap_h]
                    if move_n in self.possible_moves:
                        self.set_new_location(move_n)
                    else:
                        self.set_prev_dir(x, y)
                        self.set_new_location(self.possible_moves[num])
                elif self.prev_dir == 'NE':
                    move_ne = [self.x + self.island.gap_w, \
                        self.y - self.island.gap_h]
                    if move_ne in self.possible_moves:
                        self.set_new_location(move_ne)
                    else:
                        self.set_prev_dir(x, y)
                        self.set_new_location(self.possible_moves[num])
                elif self.prev_dir == 'E':
                    move_e = [self.x + self.island.gap_w, self.y]
                    if move_e in self.possible_moves:
                        self.set_new_location(move_e)
                    else:
                        self.set_prev_dir(x, y)
                        self.set_new_location(self.possible_moves[num])
                elif self.prev_dir == 'SE':
                    move_se = [self.x + self.island.gap_w, \
                        self.y + self.island.gap_h]
                    if move_se in self.possible_moves:
                        self.set_new_location(move_se)
                    else:
                        self.set_prev_dir(x, y)
                        self.set_new_location(self.possible_moves[num])
                elif self.prev_dir == 'S':
                    move_s = [self.x, self.y + self.island.gap_h]
                    if move_s in self.possible_moves:
                        self.set_new_location(move_s)
                    else:
                        self.set_prev_dir(x, y)
                        self.set_new_location(self.possible_moves[num])
                elif self.prev_dir == 'SW':
                    move_sw = [self.x - self.island.gap_w, \
                        self.y + self.island.gap_h]
                    if move_sw in self.possible_moves:
                        self.set_new_location(move_sw)
                    else:
                        self.set_prev_dir(x, y)
                        self.set_new_location(self.possible_moves[num])
                elif self.prev_dir == 'W':
                    move_w = [self.x - self.island.gap_w, self.y]
                    if move_w in self.possible_moves:
                        self.set_new_location(move_w)
                    else:
                        self.set_prev_dir(x, y)
                        self.set_new_location(self.possible_moves[num])
                elif self.prev_dir == 'NW':
                    move_nw = [self.x - self.island.gap_w, \
                        self.y - self.island.gap_h]
                    if move_nw in self.possible_moves:
                        self.set_new_location(move_nw)
                    else:
                        self.set_prev_dir(x, y)
                        self.set_new_location(self.possible_moves[num])
            else:
                self.breed(self.possible_moves[num])
        else:
            pass


    def reset_moved_flag(self):
        self.moved = False
        self.possible_moves = []

    
    def died(self):
        self.alive = False


class Prey(Animal):
    ''' prey class '''
    def __init__(self, island, x=0, y=0, name='Py'):
        super().__init__(island, x, y, name)
        self.name = f'Prey_{name}'
        self.type = 3
        self.breed_clock = random.randint(20, 30)
        self.move_animal
        self.died
        self.breed


    def check_possible_moves(self):
        super().check_possible_moves()
        for a in self.island.prey + self.island.pred:
            if [a.x, a.y] in self.possible_moves:
                self.possible_moves.remove([a.x, a.y])

    
    def breed(self, pos):
        self.offspring += 1
        self.breed_clock = random.randint(20, 30)
        p = len(self.island.dead_prey) + len(self.island.prey)
        self.island.prey.append(Prey(self.island, pos[0], pos[1], p))
        print(f'{self.name} gave birth to Prey_{p} on move {self.island.island_age}!')



    def died(self):
        super().died()
        self.island.dead_prey.append(self)
        self.island.prey.remove(self)


class Preditor(Animal):
    ''' preditor class '''
    def __init__(self, island, x=0, y=0, name='Pd'):
        super().__init__(island, x, y, name)
        self.name = f'Preditor_{name}'
        self.type = 5
        self.breed_clock = random.randint(25, 50)
        self.move_animal
        self.died
        self.breed
        self.starve_clock = random.randint(15, 50)


    def check_possible_moves(self):
        super().check_possible_moves()
        for a in self.island.prey:
            if [a.x, a.y] in self.possible_moves:
                self.possible_moves = ([[a.x, a.y]])
                break
        for b in self.island.pred:
            if [b.x, b.y] in self.possible_moves:
                self.possible_moves.remove([b.x, b.y])


    def move_animal(self):
        self.starve()
        if self.alive:
            super().move_animal()

            self.starve_clock -= 1

            for a in self.island.prey:
                if a.x == self.x and a.y == self.y:
                    self.starve_clock = random.randint(15, 30)
                    print(f'{self.name} ate {a.name} on move {self.island.island_age}!')
                    a.died()


    def breed(self, pos):
        self.breed_clock = random.randint(25, 50)
        p = len(self.island.dead_pred) + len(self.island.pred)
        self.island.pred.append(Preditor(self.island, pos[0], pos[1], p))
        print(f'{self.name} gave birth to Predator_{p} on move {self.island.island_age}!')


    def died(self):
        super().died()
        self.island.dead_pred.append(self)
        self.island.pred.remove(self)


    def starve(self):
        if self.starve_clock == 0:
            self.died()
            print(f'{self.name} starved on move {self.island.island_age}!')
