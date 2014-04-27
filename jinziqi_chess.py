#coding:utf8
import unittest

DEBUG = True

class Player():
    def __init__(self):
        self.avatar = ''
        self.chesses = []
    def put_chess(self, location, board):
        c = Chess(location, self)
        if board.put_chess(c):
            return c
        else:
            return None

class ChessBoard():
    def __init__(self, x, y):
        self._chesses = []
        self.load_chess_board(x, y)
    def load_chess_board(self, x, y):
        self._chesses = []
        id = 0
        for yy in range(y):
            for xx in range(x):
                self._chesses.append(Position(id, xx, yy))
                id = id + 1
        return self._chesses
    def put_chess(self, chess):
        for p in self._chesses:
            if p.id == chess.id and p.content is None:
                p.content = chess
                return True
        return False
#     def chesses(self, id):
#         return self._chesses[id]
    
class Chess():
    def __init__(self, id, owner):
        self.id = id
        self.owner = owner

class Position():
    def __init__(self, id = -1, x = -1, y = -1):
        self.id = id
        self.x = x
        self.y = y
        self.content = None
    def XY(self):
        return (self.x, self.y)

class PositionTest(unittest.TestCase):
    def setUp(self):
        self.pos = Position()

class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        self.chess_board = ChessBoard(3, 3)
    def testChessBoard(self):
        cb = ChessBoard(3, 3)
        chessboard = cb.load_chess_board(3, 3)
        self.assertTrue(isinstance(chessboard, list))
        self.assertTrue(isinstance(chessboard[0], Position))
        # Position(0, 0, 0) 
        self.assertTrue(0 == chessboard[0].id)
        self.assertTrue(0 == chessboard[0].x)
        self.assertTrue(0 == chessboard[0].y)
        # Position(1, 1, 0)
        self.assertTrue(1 == chessboard[1].id)
        self.assertTrue(1 == chessboard[1].x)
        self.assertTrue(0 == chessboard[1].y)
    def testBoardPutChess(self):
        chess1 = Chess(0, Player())
        self.assertTrue(self.chess_board.put_chess(chess1))
        self.assertFalse(self.chess_board.put_chess(chess1))

class ChessTest(unittest.TestCase):
    def setUp(self):
        self.chess = Chess(0, Player())

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()
    def testPlayerPutChess(self):
        cb = ChessBoard(3,3)
        chess = self.player.put_chess(0, cb)
        self.assertTrue(isinstance(chess, Chess))
        self.assertTrue(0 == chess.id)
        chess = self.player.put_chess(0, cb)
        self.assertTrue(None == chess)
    def testPlayerAvatar(self):
        self.player.avatar = 'X'
        self.assertTrue('X' == self.player.avatar)

if __name__ == '__main__':
    if DEBUG:
        unittest.main()
