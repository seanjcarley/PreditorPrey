class Animal:
    ''' base class for the preditor and prey classes '''
    HEAL_RATE = 5

    def __init__(self, x=0, y=0):
        self.health = 100
        self.hunger = 0   


    def reduce_health(self, damage):
        self.health -= damage
        return self.health


    def heal(self, ):
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
    pass

class Prey(Animal):
    ''' Prey class'''
    pass
