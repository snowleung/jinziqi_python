#coding:utf-8
'''
    Jinziqi Core Test Case
    ~~~~~~~~~~~~~~~~~~~~~~

    Test Cases
'''
import unittest
import itertools
from jinziqi.jinziqi import Jinziqi_core
from jinziqi.jinziqi_chess import Player, Chess
import logging

logging.basicConfig(level=logging.DEBUG)


class TestJinziqi(unittest.TestCase):
    def setUp(self):
        self.jinziqi = Jinziqi_core()
        logging.info('setup')
    def testPlayerCount(self):
        '''only 2 player
        '''
        self.assertTrue(len(self.jinziqi.players) == 2)

    def test_player(self):
        '''测试玩家
        '''
        jinziqi_program = Jinziqi_core()
        self.assertEquals([],jinziqi_program.player_a.my_chesses(jinziqi_program.cb))
        self.assertEquals([],jinziqi_program.player_b.my_chesses(jinziqi_program.cb))

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
        chessboard = jinziqi_program.get_chessboard()
        chessboard.put_chess(Chess(0, Player()))
        chessboard.put_chess(Chess(1, Player()))
        chessboard.put_chess(Chess(2, Player()))
        chessboard.put_chess(Chess(6, Player()))
        chessboard.put_chess(Chess(7, Player()))
        self.assertTrue(jinziqi_program.is_win([0,1,2,6,7]))
    def test_add_chess(self):
        jinziqi_program = Jinziqi_core('X', 'O')
        p1 = Player()
        chess = jinziqi_program.add_chess(p1, 1)
        self.assertTrue(chess.owner == p1)
        self.assertTrue(chess.id == 1)
    # def test_print_chessboard(self):
    #     jinziqi_program = Jinziqi_core('X', 'O')
    #     position = 7
    #     play_a = [1,2]
    #     play_b = [3,7]
    #     self.assertTrue('O' == jinziqi_program.print_chess(position, play_a, play_b))
    #     position = 7
    #     play_a = [1,7]
    #     play_b = [3,6]
    #     self.assertTrue('X' == jinziqi_program.print_chess(position, play_a, play_b))
    #     position = 5
    #     play_a = [1,2]
    #     play_b = [3,7]
    #     self.assertTrue('5' == jinziqi_program.print_chess(position, play_a, play_b))
