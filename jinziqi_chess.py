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
    def __init__(self):
        self._chesses = []
    def load_chesses(self, chesses_info):
        self._chesses = []
        for c in chesses_info:
            self._chesses.append(c)
    def put_chess(self, chess):
        pass
    def chesses(self):
        return self._chesses
    
class Chess(Player):
    def __init__(self, id = -1, x = 0, y = 0):
        self.id = id
        self.x = x
        self.y = y
        self.is_use = False
    def chess_XY(self):
        return (self.x, self.y)

class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        self.chess_board = ChessBoard()
    def testChessBoard(self):
        chessboard = ChessBoard()
        self.assertTrue([] == chessboard.chesses())
        self.assertTrue(0 == len(chessboard.chesses()))
    def testBoardPutChess(self):
        chess1 = Chess(1, 1, 1)
        self.assertTrue(self.chess_board.put_chess(chess1))
        self.assertFalse(self.chess_board.put_chess(chess1))
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
        self.chess_board = ChessBoard()
#         _chessboard = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
#         _chessinfo = []
#         for k,v in _chessboard.items():
#             _chessinfo.append(Chess(k, v[0], v[1]))
#         self.chess_board.load_chesses(_chessinfo)

    def testPlayerAvatar(self):
        self.player.avatar = 'X'
        self.assertTrue('X' == self.player.avatar)
    def test_chess_exists(self):
        '''can't add chess twice at the some loaction
        '''
        chess = Chess(1, 0, 0)
        self.assertTrue(self.player.add_chess(chess, self.chess_board))
        self.assertFalse(self.player.add_chess(chess, self.chess_board))

if __name__ == '__main__':
    if DEBUG:
        unittest.main()
