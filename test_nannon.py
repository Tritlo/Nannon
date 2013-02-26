import unittest
from nannon import Nannon

class testNannon(unittest.TestCase):
    
    def setUp(self):
        self.to = Nannon()

    def testCheckWin(self):
        self.to = Nannon() #: unplayed game can't be finished
        self.assertFalse(self.to.board.checkWin())
        self.to.gameLoop(1,auto=True) #after we've played the game, it should be finished
        self.assertTrue(self.to.board.checkWin())
        
    def testDie(self):
        for i in range(1000):
            self.assertIn(self.to.die.roll(),range(1,7))

                         
if __name__== '__main__':
    unittest.main(verbosity=2, exit=False)
