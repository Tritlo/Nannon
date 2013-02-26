from Die import Die
from Board import Board

class Nannon:
    
    board = None
    die = None
    points = {-1:0,1:0}
    whitePoints = 0 #: How many points white has
    blackPoints = 0#: How many points black has
    games = 0 #: Games played
    
    current = 0
    
    def __init__(self):

        self.board = Board()
        self.die = Die()
    

    def roll(self,current=0):
        """
        #Use: s.roll(s)
        #Pre: s is "initial", "black" or "white"
        #Post: Alea iacta est, according to what roll is to be made.
        """
        if current == 0:
            whiteDie = self.die.roll() 
            blackDie = self.die.roll()
            if whiteDie == blackDie:
                return self.roll()
            else:
                self.current = 1 if whiteDie < blackDie else -1
                return abs(whiteDie-blackDie)
        else:
            return self.die.roll()
       
    def gameLoop(self,gamesToPlay = 1):
        while self.games < gamesToPlay:
            self.current = 0
            gameOver = False
            roll = self.roll()
            self.current = self.current*-1
            while gameOver is False:
                self.current = self.current*-1
                roll = self.roll(self.current)
                v = self.board.validMoves(roll,self.current)
                if v == []:
                    print "%d turn. Roll %d" % (self.current, roll)
                    print "No available moves"
                    continue
                print "%d turn. Roll %d" % (self.current, roll)
                print "Board: %s %s %s" %(self.board.homes[-1], self.board.board, self.board.homes[1])
                print "Choose from the following moves"
                print v
                ch = raw_input("Choice: ")
                print
                if len(ch) == 0:
                    ch = 0
                fr,to = v[int(ch)]
                gameOver = self.board.move(fr,to)
            self.points[self.current] = self.points[self.current]+1
            self.games = self.games+1
        print self.games, self.points
                
            
if __name__=="__main__":
    nan = Nannon()
    nan.gameLoop()
    
