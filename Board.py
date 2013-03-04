class Board:
    """Class that implements the Nannon Board"""
    board = None #: The current state of the board
    home = lambda self,x: 0 if x == -1 else 7 #: Function that says what is home for black and white
    safety = lambda self,x: 7 if x == -1 else 0 #: Function that states what is safety for black and white
    homes = {-1:1,1:1} #: How many checkers are in the home base of each side
    
    def __init__(self, board = [-1,-1,0,0,1,1], homes= {-1:1,1:1}):
        """
        #Use: s = Board()
        #Pre: None
        #Post: s is a new Nannon game Board()
        """
        self.board = board
        self.homes = homes
        
    def move(self,fr,to):
        """
        #Use: b = n.move(f,t)
        #Pre: f,t are legal places to move a checker from and to on n which is a board
        #Post: a checker has been moved from f to t, b is True if the game is over
        """
        co = self.color(fr)
        self.changeFrom(fr)
        self.changeTo(to,co)
        return self.checkWin() 

    def changeFrom(self,fr):
        """
        #Use: s.changeFrom(f)
        #Pre: s is a board, f is a legal place to move from
        #Post: The checker has been moved from from
        """
        co = self.color(fr)
        ho = self.home(co)
        if fr == ho and self.homes[co] > 0:
           self.homes[co] = self.homes[co]-1
        else:
            self.board[fr-1] = 0
            
    def changeTo(self,to,col):
        """
        #Use: s.changeTo(t)
        #Pre: s is a Board, t is a legal place to move to, col is the color of the checker that is being moved
        #Post: The checker of color col has been moved to to
        """
        sa = self.safety(col)
        if to == sa:
            pass
        else:
            if self.board[to-1] != 0:
                self.homes[self.board[to-1]] = self.homes[self.board[to-1]] + 1
            self.board[to-1] = col
            
    def checkWin(self):
       """
       #Use: b = s.checkWin()
       #Pre: s is a board
       #Post: b True if the game is over else false
       """
       if (-1 not in self.board and self.homes[-1] == 0):
           return True
       if (1 not in self.board and self.homes[1] == 0):
            return True
       return False
   
    def color(self,checker):
        """
        #Use: c = s.color(ch)
        #Pre: s is a board, ch i a legal checker
        #Post: c is the color of the checker on ch, 0 if no checker there
        """
        if checker == 0 or checker == 7:
            return -1 if checker == 0 else 1
        else:
            return self.board[checker-1]

    def prime(self,fr):
        """
        #Use: b = s.prime(ch)
        #Pre: s is a board, ch i a legal checker
        #Post: b is true if the checker on fr is in a prime position, false otherwise. false for no checker.
        """
        if fr not in range(0,8):
            return False
        co = self.color(fr)
        if co == 0:
            return False
        sa = self.safety(co)
        ho = self.home(co)
        if fr == sa:
            return False
        if fr == ho:
            return (self.color(abs(ho-1)) == co) and (self.homes[co] > 0)
        return fr == abs(ho-1) and (self.homes[co] > 0 or self.color(abs(ho-2)) == co) or self.color(fr-1) == co or self.color(fr+1) == co
        

    def validTo(self,to,col):
        """
        #Use: b = s.validTo(ch)
        #Pre: s is a board, ch is a legal checker
        #Post: b is true if it is valid to move a checker of color col to to.
        """
        sa = self.safety(col)
        ho = self.home(col)
        if to not in range(0,8):
            return False
        if to == ho or to == sa:
            return (not self.prime(to))
        if (self.board[to-1] != col and not self.prime(to)):
            return True
        return False

    def __str__(self):
        """
        #Use: k  = str(s)
        #Pre: s is a board,
        #Post: k is a string representing the board
        """
        iTC = lambda  x: "w" if x == -1 else " " if x == 0 else "b"
        printList = ["w" if self.homes[-1] >=1 else " "] + map(iTC, self.board)+ [ "b" if self.homes[1] >=1 else " "]
        r = ""
        r = r + " %s   |    |    |    |    |    |   %s \n" % ("w" if self.homes[-1] >=3 else " ","b" if self.homes[1] ==3 else " ")
        r = r +  " %s  / \  /:\  / \  /:\  / \  /:\  %s  \n" % ("w" if self.homes[-1] >=2 else " ","b" if self.homes[1] >=2 else " ")
        r = r +  " %s / %s \/:%s:\/ %s \/:%s:\/ %s \/:%s:\ %s \n" % tuple(printList)
        r = r +  " W   1    2    3    4    5    6   B "
        return r

    def validMoves(self,roll,col):
        """
        #Use: b = s.validMoves(r,c)
        #Pre: s is a board, r is a integer, c is a color
        #Post: b is a list of valid moves on the board for the color c with the roll r, on the format (from,to)
        """
        val = []
        if self.homes[col] > 0:
            if self.validTo(self.home(col) - col*roll,col):
                val.append((self.home(col),self.home(col) - col*roll))
        for i,c in enumerate(self.board):
            if c != col:
                continue
            if self.validTo(i+1 - col*roll,col):
                val.append((i+1,i+1 - col*roll))
        return val
