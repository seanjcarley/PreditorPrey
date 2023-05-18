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
                        and self.type > tile.type:  # right and up
                    possible_moves.append([tile.x, tile.y])
                if tile.x == current_tile.x + self.island.gap_w \
                        and tile.y == current_tile.y + self.island.gap_h \
                        and self.type > tile.type:  # right and down
                    possible_moves.append([tile.x, tile.y])
                if tile.x == current_tile.x - self.island.gap_w \
                        and tile.y == current_tile.y - self.island.gap_h \
                        and self.type > tile.type:  # left and up
                    possible_moves.append([tile.x, tile.y])
                if tile.x == current_tile.x - self.island.gap_w \
                        and tile.y == current_tile.y + self.island.gap_h \
                        and self.type > tile.type:  # left and down
                    possible_moves.append([tile.x, tile.y])


        return possible_moves

    
    def move_animal(self):
        possible_moves = self.check_possible_moves()
        print(f'{self.name}: {possible_moves}')
        no_of_moves = len(possible_moves)

        if no_of_moves > 1:
            num = random.randint(0, no_of_moves - 1)
            self.x, self.y = possible_moves[num]
            self.moved = True
        elif no_of_moves == 1:
            self.x, self.y = possible_moves[0]
            self.moved = True


    def reset_moved_flag(self):
        self.moved = False


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

