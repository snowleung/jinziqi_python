#coding:utf8
import unittest

DEBUG = True

class Player():
    def __init__(self):
        self.avatar = ''
        self.chesses = []
    def add_chess(self, c):
        ''' c = chess
        '''
        self.chesses.append(c)

class ChessBoard():
    def __init__(self):
        self._chesses = []
    def chesses(self):
        return self._chesses


class Chess(Player):
    def __init__(self):
        self.id = -1
        self.x = 0
        self.y = 0

class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        self.chess_board = ChessBoard()
    def testChessBoard(self):
        chessboard = ChessBoard()
        self.assertTrue([] == chessboard.chesses())
        self.assertTrue(0 == len(chessboard.chesses()))

class ChessTest(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()
    def testChessLocation(self):
        self.assertTrue(0 == self.chess.x)
        self.assertTrue(0 == self.chess.y)

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()
    def testPlayerAvatar(self):
        self.player.avatar = 'X'
        self.assertTrue('X' == self.player.avatar)
    def testPlayerChesses(self):
        chess = Chess()
        self.player.add_chess(chess)
        self.assertTrue(chess in self.player.chesses)
        chess2 = Chess()
        self.assertFalse(chess2 in self.player.chesses)
        self.player.add_chess(chess2)
        self.assertTrue(chess2 in self.player.chesses)
        

if __name__ == '__main__':
    if DEBUG:
        unittest.main()
