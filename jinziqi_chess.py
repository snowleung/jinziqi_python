#coding:utf8
import unittest

DEBUG = True

class Player():
    def __init__(self):
        self.avatar = ''
        self.chesses = []
    def add_chess(self, c, board):
        '''
        c = chess
        board = chessboard
        '''
        chess = board.chesses(c.id)
        if chess == None:
            self.chesses.append(c)
            board.put_chess(c)
            return True
        else:
            return False

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
    
class Chess(Player):
    def __init__(self, id = -1, x = 0, y = 0):
        self.id = id
        self.x = x
        self.y = y
        self.is_use = False
    def chess_XY(self):
        return (self.x, self.y)

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
        chess1 = Chess(1, 1, 1)
        self.assertTrue(self.chess_board.put_chess(chess1))
        self.assertFalse(self.chess_board.put_chess(chess1))

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
#         self.chess_board = ChessBoard()
#         _chessboard = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
#         _chessinfo = []
#         for k,v in _chessboard.items():
#             _chessinfo.append(Chess(k, v[0], v[1]))
#         self.chess_board.load_chesses(_chessinfo)

    def testPlayerAvatar(self):
        self.player.avatar = 'X'
        self.assertTrue('X' == self.player.avatar)
#     def test_chess_exists(self):
#         '''can't add chess twice at the some loaction
#         '''
#         chess = Chess(1, 0, 0)
#         self.assertTrue(self.player.add_chess(chess, self.chess_board))
#         self.assertFalse(self.player.add_chess(chess, self.chess_board))

if __name__ == '__main__':
    if DEBUG:
        unittest.main()
