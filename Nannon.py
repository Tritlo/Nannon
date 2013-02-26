from Die import Die
from Board import Board

class Nannon:
    """A class that implements the Nannon game"""    
    board = None #: The board the game is played on
    die = None #: The die used to play the game
    points = {-1:0,1:0} #: How many points each side has. Note, -1 is used to represent white, and 1 black
    games = 0 #: Games played
    current = 0 #: The current player. 0 at start of game
    intToColor = lambda self, x: "white" if x == -1 else "none" if x == 0 else "black"
    def __init__(self):
        """
        #Use: s = Nannon()
        #Pre: None
        #Post: s is a new Nannon game
        """
        self.board = Board()
        self.die = Die()
    
        self.points = {-1:0,1:0}
        self.games = 0 

        self.current = 0
        
    def roll(self,current=0):
        """
        #Use: k = s.roll(j)
        #Pre: s is a Nannon game.
        #Post: Alea iacta est. The dies are cast for the initial throw if current is 0, or just rolled if current is something else/not provided
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
        
    def getInput(self,lv):
        """
        #Use: ch = s.getInput(i)
        #Pre: i is an integer
        #Post: ch is an integer from stdin in [0,...,lv]
        """
        try:
            ch = raw_input("Choice: ")
            if len(ch) == 0:
                ch = 0
            ch = int(ch)
            if ch not in range(lv):
                raise ValueError
            return ch
        except ValueError:
            print "Invalid choice!"
            self.getInput(lv)
        
       
    def gameLoop(self,gamesToPlay = 1, auto = False):
        """
        #Use: s.gameLoop(i,a)
        #Pre: i is an integer, a is boolean, both optional
        #Post: The game has been played for i rounds, 1 if i not provided, automatically if auto is True
        """
        while self.games < gamesToPlay:
            self.board = Board()
            self.current = 0
            gameOver = False
            while gameOver is False:
                self.current = self.current*-1
                roll = self.roll(self.current)
                v = self.board.validMoves(roll,self.current)
                if v == []:
                    print "It is %s's turn. Roll %d" % (self.intToColor(self.current), roll)
                    print "No available moves"
                    print 
                    continue
                print "It is %s's turn. Roll %d" % (self.intToColor(self.current), roll)
                iTC = lambda  x: "w" if x == -1 else " " if x == 0 else "b"
                print "Board:\n %s %s %s" %(self.board.homes[-1], map(iTC, self.board.board), self.board.homes[1])
                print " W   1    2    3    4    5    6   B"
                print "Choose from the following moves (default 0)"
                self.printMoves(v,self.current)
                ch = self.getInput(len(v)+1) if not auto else 0
                fr,to = v[int(ch)]
                gameOver = self.board.move(fr,to)
                print
            self.points[self.current] = self.points[self.current]+1
            print "The winner of this round is %s!" % (self.intToColor(self.current))
            self.games = self.games+1
            print
        winner = -1 if self.points[-1] > self.points[1] else 0 if self.points[-1] == self.points[1] else 1
        pointString = (self.points[winner],self.points[winner*-1]) if winner != 0 else (self.points[1],self.points[1])
        print "The final winner is %s with %s points, after %d games" % (self.intToColor(winner), "%d to %d" % pointString ,self.games)

    def printMoves(self,moves,color):
        for i,r in enumerate(moves):
            f,t = r
            chart = dict(zip(range(1,7),range(1,7)))
            chart[self.board.home(color)] = "home"
            chart[self.board.safety(color)] =  "safety"
            print "Move %d: Move checker from %s to %s" %(i,str(chart[f]),str(chart[t]))
            
if __name__=="__main__":
    nan = Nannon()
    nan.gameLoop(100,True)
    
