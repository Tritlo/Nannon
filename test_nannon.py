import unittest
from nannon import Nannon
from Board import Board

class testNannon(unittest.TestCase):
    
    def setUp(self):
        self.to = Nannon()
        self.bo = Board(board = [-1,-1,0,0,1,1],homes = {-1:1,1:1})
        self.bo2 = Board(board = [-1,-1,0,1,0,1],homes = {-1:1,1:1})
        
    def testCheckWin(self):
        self.to = Nannon() #: unplayed game can't be finished
        self.assertFalse(self.to.board.checkWin())
        self.to.gameLoop(1,auto=True) #after we've played the game, it should be finished
        self.assertTrue(self.to.board.checkWin())
        self.to.newGame(auto=True)
        self.assertFalse(self.to.board.checkWin())
        
    def testDie(self):
        for i in range(1000):
            self.assertIn(self.to.die.roll(),range(1,7))
        k = 1000000
        s = float(0)
        for i in range(k):
            s = s + self.to.die.roll()/float(k)
        self.assertAlmostEqual(s,3.5,2)

    def testValidMoves(self):
        self.assertIn((1,3),self.bo.validMoves(2,-1))
        self.assertNotIn((2,5),self.bo.validMoves(3,-1))
        self.assertNotIn((2,6),self.bo.validMoves(4,-1))
        self.assertNotIn((2,1),self.bo.validMoves(4,-1))
        self.assertNotIn((2,3),self.bo.validMoves(4,-1))
        self.assertNotIn((1,7),self.bo.validMoves(6,-1))
        self.assertNotIn((6,0),self.bo.validMoves(6,1))
        self.assertIn((2,4),self.bo2.validMoves(2,-1))

    def testConsequences(self):
        boTemp = Board(board = [-1,-1,0,1,0,1],homes = {-1:1,1:1})
        self.assertIn((2,4),boTemp.validMoves(2,-1))
        boTemp.move(2,4)
        self.assertDictEqual(boTemp.homes,{-1:1,1:2})
        self.assertListEqual(boTemp.board,[-1,0,0,-1,0,1])
        
    def testPrime(self):
        self.assertTrue(self.bo.prime(5))
        self.assertTrue(self.bo.prime(6))
        self.assertTrue(self.bo2.prime(6))
        self.assertFalse(self.bo2.prime(4))

    def testColor(self):
        self.assertEqual(-1,self.bo.color(1)) 
                         
if __name__== '__main__':
    unittest.main(verbosity=2, exit=False)
