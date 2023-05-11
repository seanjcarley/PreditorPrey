class Animal:
    ''' base class for the preditor and prey classes '''
    HEAL_RATE = 5

    def __init__(self, x=0, y=0, type='A'):
        self.health = 100
        self.hunger = 0
        self.type = type
        self.x = x
        self.y = y
        self.moved = False

    
    def get_pos(self):
        pass

    
    def move(self):
        ''' function to check the surrounding 8 squares and move the Animal if 
        applicable
        '''

        pass
            


    def reduce_health(self, damage):
        self.health -= damage
        return self.health


    def heal(self):
        if self.hunger < 6 and self.health > 50:
            if self.health - self.HEAL_RATE < 0:
                self.health = 0
            else:
                self.health -= self.HEAL_RATE


    def reduce_hunger(self, food):
        if self.hunger < 100:
            if self.hunger - food < 0:
                self.hunger = 0
                self.health 
            else:
                self.hunger += food

class Preditor(Animal):
    ''' Preditor class'''
    def __init__(self):
        super.__init__()

# class Prey(Animal):
#     ''' Prey class'''
#     pass
