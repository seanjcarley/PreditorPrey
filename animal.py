class Animal:
    ''' parent class for preditor and prey classes '''
    def __init__(self, island, x=0, y=0, name="A"):
        self.island = island
        self.x = x
        self.y = y
        self.name = name
        self.moved = False
        self.type = 7

    
    def __str__(self):
        ''' return the object name '''
        return self.name
    

    def __repr__(self):
        ''' returns printable representation of specified object '''
        return self.__str__()
