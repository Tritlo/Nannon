from Die import Die
from Board import Board

class Nannon:
    """A class that implements the Nannon game"""    
    board = None #: The board the game is played on
    die = None #: The die used to play the game
    points = {-1:0,1:0} #: How many points each side has. Note, -1 is used to represent white, and 1 black
    games = 0 #: Games played
    current = 0 #: The current player. 0 at start of game
    intToColor = lambda self, x: "white" if x == -1 else "tied" if x == 0 else "black"
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
        
    def getInput(self,lv=None):
        """
        #Use: ch = s.getInput(i)
        #Pre: i is an integer,  s is a Nannon object
        #Post: ch is an integer from stdin in [0,...,lv]
        """
        try:
            ch = raw_input("Choice: ")
            if len(ch) == 0:
                ch = 0
            ch = int(ch)
            if lv is not None:
                if ch not in range(lv):
                    raise ValueError
            return ch
        except ValueError:
            print "Invalid choice!"
            return self.getInput(lv)

    def newGame(self,auto=False):
        """
        #Use: s.newGame(a)
        #Pre: a is boolean
        #Post: The gameboard has been set up for a new game, and a messaged printed if the optional auto is false
        """
        if not auto:
            print "New game, game %d \n\n" % (self.games)
        self.board = Board([-1,-1,0,0,1,1],{-1:1,1:1})
        self.current = 0
        self.gameOver = False
        
       
    def gameLoop(self,gamesToPlay = 1, auto = False):
        """
        #Use: s.gameLoop(i,a)
        #Pre: i is an integer, a is boolean, both optional
        #Post: The game has been played for i rounds, 1 if i not provided, automatically if auto is True
        """
        while self.games < gamesToPlay:
            self.newGame(auto)
            while self.gameOver is False:
                self.current = self.current*-1
                roll = self.roll(self.current)
                v = self.board.validMoves(roll,self.current)
                if v == []:
                    if not auto:
                        print "It's %s's turn. The roll was %d." % (self.intToColor(self.current), roll)
                        print "No available moves."
                        print 
                    continue
                if not auto:
                    print "It's %s's turn. The roll was %d." % (self.intToColor(self.current), roll)
                    print self.board
                    print "Choose from the following moves (default 0):"
                    self.printMoves(v,self.current)
                ch = self.getInput(len(v)+1) if not auto else 0 #Biased for black, len(v)-1 is biased for white
                fr,to = v[int(ch)]
                self.gameOver = self.board.move(fr,to)
                if not auto:
                    print
            self.points[self.current] = self.points[self.current]+1
            if not auto:
                print "The winner of this round is %s!" % (self.intToColor(self.current))
                self.printScore
            self.games = self.games+1

    def printScore(self):
        """
        #Use: s.printScore()
        #Pre: s i s a Nannon object
        #Post: The current score has been printed 
        """
        winner = -1 if self.points[-1] > self.points[1] else 0 if self.points[-1] == self.points[1] else 1
        pointString = (self.points[winner],self.points[winner*-1]) if winner != 0 else (self.points[1],self.points[1])
        print "The score is %s with %s points, after %d games." % (self.intToColor(winner), "%d to %d" % pointString ,self.games)

    def printMoves(self,moves,color):
        """
        #Use: s.printMoves(m,c)
        #Pre: s is a nannon object, m is a list of valid moves, color is the color of the player who can preform the moves
        #Post: The current score has been printed 
        """
        for i,r in enumerate(moves):
            f,t = r
            chart = dict(zip(range(-6,0)+range(1,7)+range(8,13),["safety" for k in range(-6,0)] + range(1,7)+["safety" for h in range(8,13)]))
            chart[self.board.home(color)] = "home"
            chart[self.board.safety(color)] =  "safety"
            print " %d: Move %s checker from %s to %s" %(i,self.intToColor(color),str(chart[f]),str(chart[t]))
        for k in range(i,2):
            print
            
if __name__=="__main__":
    nan = Nannon()
    #nan.gameLoop(100,True)
    print "How many games do you want to play (default 0)?"
    g = nan.getInput()
    nan.gameLoop(g,False)
    if g > 0:
        nan.printScore()
    else:
        print "Goodbye!"
    
