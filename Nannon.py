import random

class Nannon:

    board = {} #: Keeps the position of the checkers. 0 is empty, 1 is white and 2 is black.
    WhiteHome = 0 #: Home of the white pieces on the board.
    BlackHome = 7 #: Home of the white pieces on the board.
    whiteDie = 0 #: holds the value of the white die
    blackDie = 0 #: holds the value of the black die
    

    
    def __init__(self, board = [1,1,1,0,0,2,2,2], WhiteHome = 0, BlackHome = 7):
        """
        #Use: s = Nannon(l,wh,bh)
        #Pre: l is a list of initial position in a Nannon game, wh is where the white home is to be located, bh is where the black home is to be located
        #Post: s is a new Nannon game
        """
        self.board =dict(zip([i for i in range(len(board))],board))
        self.WhiteHome = WhiteHome
        self.BlackHome = BlackHome
        self.whiteDie = 0
        self.blackDie = 0
    

    def roll(self,roll="initial"):
        """
        #Use: s.roll(s)
        #Pre: s is "initial", "black" or "white"
            #Post: Alea iacta est, according to what roll is to be made.
        """
        if roll == "initial":
            self.whiteDie = random.randint(1,6)
            self.blackDie = random.randint(1,6)
            if self.whiteDie == self.blackDie:
                self.roll()
       if roll == "black": 
            self.blackDie = random.randint(1,6)
       if roll == "white": 
            self.whiteDie = random.randint(1,6)
