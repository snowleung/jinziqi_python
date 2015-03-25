#coding:utf-8


class Player():
    def __init__(self):
        self.avatar = ''
    def put_chess(self, location, board):
        c = Chess(location, self)
        if board.put_chess(c):
            return c
        else:
            return None
    def my_chesses(self, board):
        return board.get_player_chesses(self)

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
    def is_full(self):
        for c in self._chesses:
            if c.content == None:
                return False
        return True
    def put_chess(self, chess):
        for p in self._chesses:
            if p.id == chess.id and p.content is None:
                p.content = chess
                return True
        return False
    def get_chess(self, id):
        chess = None
        for p in self._chesses:
            if p.id == id and p.content is not None:
                chess = p
        return chess
    def get_player_chesses(self, player):
        chesses = []
        for p in self._chesses:
            if p.content and p.content.owner == player:
                chesses.append(p.content)
        return chesses
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
