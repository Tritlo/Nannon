from random import randint as r

class Die:

    sides = 6 #: Number of sides the die has

    def __init__(self,sides = 6):
        self.sides = sides

    def roll(self):
        return r(1,self.sides)
