from random import randint as r

class Die:
"""Class that implements a die"""
    sides = 6 #: Number of sides the die has

    def __init__(self,sides = 6):
        """
        #Use: s = Die(k)
        #Pre: None, k optionally an integer
        #Post: s is a Die with k sides.
        """
        self.sides = sides

    def roll(self):
        return r(1,self.sides)
