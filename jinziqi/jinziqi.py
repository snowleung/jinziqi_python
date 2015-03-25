#coding:utf8
from jinziqi_chess import Player, ChessBoard
import itertools


class Jinziqi_core():
    def __init__(self, player_a_tag = 'A', player_b_tag = 'B'):
        self.players = []
        self.player_a = Player()
        self.player_a.avatar = player_a_tag
        self.player_b = Player()
        self.player_b.avatar = player_b_tag
        self.players.append(self.player_a)
        self.players.append(self.player_b)
        self.x = 3
        self.cb = ChessBoard(self.x, self.x)

    def print_chessboard(self):                         
        cbc = self.cb._chesses
        step = 1
        for c in cbc:
            if c.content == None:
                print c.id,
            else:
                print c.content.owner.avatar,
            if step == self.x:
                step = 1
                print ''
                continue
            step = step + 1
    def add_chess(self, player, location):
        return player.put_chess(location, self.cb)
    def exit_jinziqi(self, info):
        self.print_chessboard()
        who = info
        print "%s is win" % who
        print 'congratulation %s please run the program again' % who
        exit(0)
    def jinziqi_start2(self):
        '''
        input: player,location
        '''
        while(1):
            self.print_chessboard()
            str_in = input('enter player, location')
            player, location = str_in.split(',')
            location = int(location)
            if player == 'a':
                self.add_chess(self.player_a, location)
                if self.is_win([c.id for c in self.player_a.my_chesses(self.cb)]):
                    self.exit_jinziqi('p1')
            if player == 'b':
                self.add_chess(self.player_b, location)
                if self.is_win([c.id for c in self.player_b.my_chesses(self.cb)]):
                    self.exit_jinziqi('p2')
            if self.cb.is_full():
                print 'no one win'
    def is_win(self, p):
        combinations = self.player_chesses_combinations(p)
        #cb = [self.chessboard(c) for c in combinations] # 有坐标的棋子集合
        for chesses in combinations:
            a = self.chessboard(chesses[0])
            b = self.chessboard(chesses[1])
            c = self.chessboard(chesses[2])
            if self.isline(a, b, c):
                return True
        return False
    def get_chessboard(self):
        return self.cb
    def player_chesses_combinations(self, player, c = 3 ):
        return tuple(itertools.combinations(player, c))
    def chessboard(self, t):
        _ch = self.cb.get_chess(t)
        convert_obj = None
        if _ch:
            convert_obj = (_ch.x, _ch.y)
        return convert_obj
    def isline(self, a, b, c):
        if self._isline_x(a,b,c):
            return True
        if self._isline_y(a,b,c):
            return True
        if self._isline_xy_1(a,b,c):
            return True
        if self._isline_xy_2(a,b,c):
            return True
        return False
    def _isline_x(self, a, b, c):
        if a[0] == b[0] :
            if b[0] == c[0]:
                return True
            else:
                return False
        else:
            return False
    def _isline_y(self, a, b, c):
        if a[1] == b[1] :
            if b[1] == c[1]:
                return True
            else:
                return False
        else:
            return False
    def _isline_xy_1(self, a, b, c):
        #y=x
        c = [a,b,c]
        result = True
        for x,y in c:
            if x==y:
                result = True
            else:
                result = False
                break
        return result
    def _isline_xy_2(self, a, b, c):
        #y = 2-x
        c = [a,b,c]
        result = True
        for x,y in c:
            if y == (2-x):
                result = True
            else:
                result = False
                break
        return result


if __name__ == '__main__':
    jinziqi_program = Jinziqi_core()
    jinziqi_program.jinziqi_start2()

