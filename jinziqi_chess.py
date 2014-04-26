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
    def load_chesses(self, chesses_info):
        for c in chesses_info:
            self._chesses.append(c)
    def chesses(self, id = None):
        if id == None:
            return self._chesses
        for c in self._chesses:
            if c.id == id:
                return c
        return None

class Chess(Player):
    def __init__(self, id = -1, x = 0, y = 0):
        self.id = id
        self.x = x
        self.y = y
    def chess_XY(self):
        return (self.x, self.y)

class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        self.chess_board = ChessBoard()
    def testChessBoard(self):
        chessboard = ChessBoard()
        self.assertTrue([] == chessboard.chesses())
        self.assertTrue(0 == len(chessboard.chesses()))
    def testLoadChesses(self):
        #jinziqi rule
        _chessboard = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
        _chessinfo = []
        for k,v in _chessboard.items():
            _chessinfo.append(Chess(k, v[0], v[1]))
        self.chess_board.load_chesses(_chessinfo)
        self.assertTrue(1 == self.chess_board.chesses(1).id)
        self.assertTrue(2 == self.chess_board.chesses(2).id)
        self.assertTrue(3 == self.chess_board.chesses(3).id)
        self.assertTrue(4 == self.chess_board.chesses(4).id)
        self.assertTrue(5 == self.chess_board.chesses(5).id)
        self.assertTrue(6 == self.chess_board.chesses(6).id)
        self.assertTrue(7 == self.chess_board.chesses(7).id)
        self.assertTrue(8 == self.chess_board.chesses(8).id)
        self.assertTrue(9 == self.chess_board.chesses(9).id)


class ChessTest(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()
    def testChessLocation(self):
        self.assertTrue(0 == self.chess.x)
        self.assertTrue(0 == self.chess.y)
    def testChessXY(self):
        ch = Chess(1, 0, 0)
        self.assertTrue((0,0), ch.chess_XY())

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
