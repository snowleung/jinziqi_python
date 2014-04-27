#coding:utf8
import unittest
import itertools
from jinziqi_chess import Player, Chess, ChessBoard

DEBUG = True

class Jinziqi_core():
    def __init__(self, player_a_tag = 'X', player_b_tag = 'O'):
        self.players = []
        self.player_a = Player()
        self.player_a.avatar = player_a_tag
        self.player_b = Player()
        self.player_b.avatar = player_b_tag
        self.players.append(self.player_a)
        self.players.append(self.player_b)
        self.cb = ChessBoard(3,3)
        self.chesses = []
    def print_chess(self, pos, pa, pb):
        if pos in pa:
            return self.player_a.avatar
        elif pos in pb:
            return self.player_b.avatar
        else:
            return str(pos)

    def print_chessboard(self, pa, pb):
        chessboard = [(1,2,3), (4,5,6), (7,8,9)]
        chessboard.reverse()
        for l in chessboard:
            for i in l:
                print self.print_chess(i, pa, pb),
            print ''

    def exit_jinziqi(self, info):
        who = info
        print "%s is win" % who
        print 'congratulation %s please run the program again' % who
        exit(0)
    def jinziqi_start(self):
        print 'game start, use 1-9 to play'
        flag = 0                # who to play now
        for i in range(1,10):
            self.print_chessboard(self.player_a.chesses, self.player_b.chesses)
            while True:
                if i%2 != 0:
                    who = 'player A'
                    flag = 0
                else:
                    who = 'player B'
                    flag = 1
                output_str = 'Now %s, select(%s): ' % (who, self.chesses_total())
                n = input(output_str)
                if self.add_chess(n):
                    if flag == 0:
                        self.player_a.chesses.append(n)
                        if self.is_win(self.player_a.chesses):
                            self.exit_jinziqi(who)
                        else:
                            break
                    else:
                        self.player_b.chesses.append(n)
                        if self.is_win(self.player_b.chesses):
                            self.exit_jinziqi(who)
                        else:
                            break
                else:
                    print 'choose the bad chess,do it again'
        print '平手了,重启程序再玩一次'

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
    def chesses_total(self):
        a = set(range(1,10))
        b = set(self.chesses)
        return list(a - b)
    def add_chess(self, ch):
        if ch < 1 or ch > 9 :
            return False
        if ch not in (self.chesses):
            self.chesses.append(ch)
            return True
        else:
            return False
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

class JinziqiTest(unittest.TestCase):
    def setUp(self):
        self.jinziqi = Jinziqi_core()
    def testPlayerCount(self):
        '''only 2 player
        '''
        self.assertTrue(len(self.jinziqi.players) == 2)

    def test_player(self):
        '''测试玩家
        '''
        jinziqi_program = Jinziqi_core()
        self.assertEquals([],jinziqi_program.player_a.chesses)
        self.assertEquals([],jinziqi_program.player_b.chesses)
#     def test_coord_range(self):
#         '''测试棋子对应的坐标
#         '''
#         jinziqi_program = Jinziqi_core()
#         self.assertTrue((0,0) == jinziqi_program.chessboard(1))
#         self.assertTrue((0,1) == jinziqi_program.chessboard(2))
#         self.assertTrue((0,2) == jinziqi_program.chessboard(3))
#         self.assertTrue((1,0) == jinziqi_program.chessboard(4))
#         self.assertTrue((1,1) == jinziqi_program.chessboard(5))
#         self.assertTrue((1,2) == jinziqi_program.chessboard(6))
#         self.assertTrue((2,0) == jinziqi_program.chessboard(7))
#         self.assertTrue((2,1) == jinziqi_program.chessboard(8))
#         self.assertTrue((2,2) == jinziqi_program.chessboard(9))
    def test_line_x(self):
        '''测试坐标是否符合一条横直线
        '''
        jinziqi_program = Jinziqi_core()
        chessboard = jinziqi_program.get_chessboard()
        chessboard.put_chess(Chess(0, Player()))
        a = jinziqi_program.chessboard(0)
        chessboard.put_chess(Chess(1, Player()))
        b = jinziqi_program.chessboard(1)
        chessboard.put_chess(Chess(2, Player()))
        c = jinziqi_program.chessboard(2)
        self.assertTrue(jinziqi_program.isline(a, b, c))
        chessboard.put_chess(Chess(1, Player()))
        a = jinziqi_program.chessboard(1)
        chessboard.put_chess(Chess(8, Player()))
        b = jinziqi_program.chessboard(8)
        chessboard.put_chess(Chess(3, Player()))
        c = jinziqi_program.chessboard(3)
        self.assertFalse(jinziqi_program.isline(a, b, c))
    def test_line_y(self):
        '''测试坐标是否符合一条纵直线
        '''
        jinziqi_program = Jinziqi_core()
        chessboard = jinziqi_program.get_chessboard()
        chessboard = jinziqi_program.get_chessboard()
        chessboard.put_chess(Chess(1, Player()))
        chessboard.put_chess(Chess(4, Player()))
        chessboard.put_chess(Chess(7, Player()))
        a = jinziqi_program.chessboard(1)
        b = jinziqi_program.chessboard(4)
        c = jinziqi_program.chessboard(7)
        self.assertTrue(jinziqi_program.isline(a, b, c))
    def test_line_xy(self):
        '''测试方程y=x和y=2-x两条直线
        '''
        jinziqi_program = Jinziqi_core()
        chessboard = jinziqi_program.get_chessboard()
        chessboard.put_chess(Chess(0, Player()))
        chessboard.put_chess(Chess(4, Player()))
        chessboard.put_chess(Chess(8, Player()))
        a = jinziqi_program.chessboard(0)
        b = jinziqi_program.chessboard(4)
        c = jinziqi_program.chessboard(8)
        self.assertTrue(jinziqi_program.isline(a, b, c))
        chessboard.put_chess(Chess(6, Player()))
        chessboard.put_chess(Chess(4, Player()))
        chessboard.put_chess(Chess(2, Player()))
        a = jinziqi_program.chessboard(6)
        b = jinziqi_program.chessboard(4)
        c = jinziqi_program.chessboard(2)
        self.assertTrue(jinziqi_program.isline(a, b, c))
    def test_chess_exists(self):
        '''
        '''
        jinziqi_program = Jinziqi_core()
        self.assertTrue(jinziqi_program.add_chess(1))
        self.assertTrue(jinziqi_program.add_chess(2))
        self.assertFalse(jinziqi_program.add_chess(1))
    def test_chess_range(self):
        '''测试棋盘中可用的位置
        '''
        jinziqi_program = Jinziqi_core()
        self.assertFalse(jinziqi_program.add_chess(10))
        self.assertFalse(jinziqi_program.add_chess(0))
        self.assertFalse(jinziqi_program.add_chess(-1))
    def test_chess_total(self):
        '''测试棋盘中剩余的空格
        '''
        jinziqi_program = Jinziqi_core()
        jinziqi_program.add_chess(9)
        jinziqi_program.add_chess(8)
        self.assertTrue([1,2,3,4,5,6,7] == jinziqi_program.chesses_total())
    def test_chesses_combinations(self):
        '''测试棋子的组合
        '''
        jinziqi_program = Jinziqi_core()
        a = jinziqi_program.player_chesses_combinations([1,2,3,4,5])
        b = tuple(itertools.combinations([1,2,3,4,5], 3))
        self.assertTrue(b == a)
    def test_win(self):
        '''测试检测获胜的判断
        '''
        jinziqi_program = Jinziqi_core()
        self.assertTrue(jinziqi_program.is_win([1,2,3,7,8]))
        self.assertTrue(jinziqi_program.is_win([7,8,9,5]))
        self.assertFalse(jinziqi_program.is_win([1,2,7,8]))
    def test_chess_tag(self):
        jinziqi_program = Jinziqi_core() # test default value
        self.assertTrue('X' == jinziqi_program.player_a.avatar)
        self.assertTrue('O' == jinziqi_program.player_b.avatar)
        jinziqi_program = Jinziqi_core('O', 'X')
        self.assertTrue('O' == jinziqi_program.player_a.avatar)
        self.assertTrue('X' == jinziqi_program.player_b.avatar)
    def test_print_chessboard(self):
        jinziqi_program = Jinziqi_core('X', 'O')
        position = 7
        play_a = [1,2]
        play_b = [3,7]
        self.assertTrue('O' == jinziqi_program.print_chess(position, play_a, play_b))
        position = 7
        play_a = [1,7]
        play_b = [3,6]
        self.assertTrue('X' == jinziqi_program.print_chess(position, play_a, play_b))
        position = 5
        play_a = [1,2]
        play_b = [3,7]
        self.assertTrue('5' == jinziqi_program.print_chess(position, play_a, play_b))


if __name__ == '__main__':
    if DEBUG:
        unittest.main()
    else:
        jinziqi_program = Jinziqi_core()
        jinziqi_program.jinziqi_start()

