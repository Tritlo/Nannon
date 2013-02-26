class Board:

    board = [-1,-1,0,0,1,1]
    home = lambda self,x: 0 if x == -1 else 7
    safety = lambda self,x: 7 if x == -1 else 0
    homes = {-1:1,1:1}
    
    def __init__(self):
        self.board = [-1,-1,0,0,1,1]

    def move(self,fr,to):
        co = self.color(fr)
        self.changeFrom(fr)
        self.changeTo(to,co)
        return self.checkWin() 

    def changeFrom(self,fr):
        co = self.color(fr)
        ho = self.home(co)
        if fr == ho and self.homes[co] > 0:
           self.homes[co] = self.homes[co]-1
        else:
            self.board[fr-1] = 0
            
    def changeTo(self,to,col):
        sa = self.safety(col)
        if to == sa:
            print "%d safe!" %(col)
        else:
            if self.board[to-1] != 0:
                self.homes[self.board[to-1]] = self.homes[self.board[to-1]] + 1
            self.board[to-1] = col
            
    def checkWin(self):
       if -1 not in self.board and self.homes[-1] == 0:
           return True
       if 1 not in self.board and self.homes[1] == 0:
           return True
       return False
   
    def color(self,checker):
        if checker == 0 or checker == 7:
            return -1 if checker == 0 else 1
        else:
            return self.board[checker-1]

    def prime(self,fr):
        return False
        co = self.color(fr)
        sa = self.safety(co)
        ho = self.home(co)
        if fr == ho:
            return False
        if fr == sa:
            return False

    def validTo(self,to,col):
        sa = self.safety(col)
        ho = self.home(col)
        if to not in range(0,8):
            return False
        if to == sa or to == ho:
            return True
        if (self.board[to-1] != col and not self.prime(to)):
            return True
        return False

    def validMoves(self,roll,col):
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

           

        
