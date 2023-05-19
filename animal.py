import random

class Animal:
    ''' parent class for preditor and prey classes '''
    def __init__(self, island, x=0, y=0, name='A'):
        self.island = island
        self.x = x
        self.y = y
        self.name = f'Animal_{name}'
        self.type = 7
        self.alive = True
        self.moved = False
        self.age = 0

    
    def __str__(self):
        ''' return the object name '''
        return self.name
    

    def __repr__(self):
        ''' returns printable representation of specified object '''
        return self.__str__()

    
    def check_possible_moves(self):
        possible_moves = []
        current_tile = None
        if self.alive and not self.moved:
            for tile in self.island.tiles:
                if tile.x == self.x and tile.y == self.y:
                    current_tile = tile
                    break

            for tile in self.island.tiles:
                if tile.x == current_tile.x + self.island.gap_w \
                        and tile.y == current_tile.y \
                        and self.type > tile.type:  # right
                    possible_moves.append([tile.x, tile.y])
                if tile.x == current_tile.x - self.island.gap_w \
                        and tile.y == current_tile.y \
                        and self.type > tile.type:  # left
                    possible_moves.append([tile.x, tile.y])
                if tile.x == current_tile.x \
                        and tile.y == current_tile.y + self.island.gap_h \
                        and self.type > tile.type:  # down
                    possible_moves.append([tile.x, tile.y])
                if tile.x == current_tile.x \
                        and tile.y == current_tile.y - self.island.gap_h \
                        and self.type > tile.type:  # up
                    possible_moves.append([tile.x, tile.y])
                if tile.x == current_tile.x + self.island.gap_w \
                        and tile.y == current_tile.y - self.island.gap_h \
                        and self.type > tile.type \
                        and current_tile.type != 2:  # right and up
                    possible_moves.append([tile.x, tile.y])
                if tile.x == current_tile.x + self.island.gap_w \
                        and tile.y == current_tile.y + self.island.gap_h \
                        and self.type > tile.type \
                        and current_tile.type != 2:  # right and down
                    possible_moves.append([tile.x, tile.y])
                if tile.x == current_tile.x - self.island.gap_w \
                        and tile.y == current_tile.y - self.island.gap_h \
                        and self.type > tile.type \
                        and current_tile.type != 2:  # left and up
                    possible_moves.append([tile.x, tile.y])
                if tile.x == current_tile.x - self.island.gap_w \
                        and tile.y == current_tile.y + self.island.gap_h \
                        and self.type > tile.type \
                        and current_tile.type != 2:  # left and down
                    possible_moves.append([tile.x, tile.y])

        return possible_moves

    
    def move_animal(self):
        possible_moves = self.check_possible_moves()
        no_of_moves = len(possible_moves)
        self.age += 1

        if self.type == 5:
            for a in self.island.prey:
                if a.x == self.x and a.y == self.y:
                    print(f'{self.name} ate {a.name}!')
                    a.died()
        
        if no_of_moves > 1:
            num = random.randint(0, no_of_moves - 1)
            self.x, self.y = possible_moves[num]
            self.moved = True
        elif no_of_moves == 1:
            self.x, self.y = possible_moves[0]
            self.moved = True


    def reset_moved_flag(self):
        self.moved = False

    
    def died(self):
        self.alive = False
        if self.type == 3:
            self.island.dead_prey.append(self)
            self.island.prey.remove(self)
        elif self.type == 5:
            self.island.dead_pred.append(self)
            self.island.pred.remove(self)
        print(f'{self.name} reached {self.age} moves, and sadly passed away!')

    
    def breed(self):
        pass


class Prey(Animal):
    ''' prey class '''
    def __init__(self, island, x=0, y=0, name='Py'):
        super().__init__(island, x, y, name)
        self.name = f'Prey_{name}'
        self.type = 3
        self.move_animal


class Preditor(Animal):
    ''' preditor class '''
    def __init__(self, island, x=0, y=0, name='Pd'):
        super().__init__(island, x, y, name)
        self.name = f'Preditor_{name}'
        self.type = 5
        self.move_animal
