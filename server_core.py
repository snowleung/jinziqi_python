#coding:utf-8

import unittest
import socket

DEBUG = True

class Core_TCP():
    def __init__(self, role = 'Server'):
        self.role = role
        self.clients = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    def start_client(self, host, port):
        self.s.connect((host, port))
        self.s.send('something')
        data = self.s.recv(1024)
        print 'i recv %s' % data
    def start_server(self):
        host = 'localhost'
        port = 11234
        self.s.bind((host, port))
        self.s.listen(3)
        while True:
            client, ipaddr = self.s.accept()
            print "connect from %s " % str(ipaddr)
            data = client.recv(1024)
            print "data is %s " % data
            client.send("echo")
            client.close()
    def regist_server(self, stream):
        prefx, types, info = stream.split(',') # 解析过程
        game_data = Game_data(prefx, types, info)
        self.clients.append(game_data)
        return game_data
    def match_game(self):
        matches = []
        for g in self.clients:
            if len(matches) < 2 and g.client == None:
                matches.append(g)
        c1, c2 = matches
        c1.client = c2
        c2.client = c1

class Core_TCPTest(unittest.TestCase):
    def setUp(self):
        self.ser = Core_TCP()
    def testClientList(self):
        self.assertTrue(len(self.ser.clients) == 0)
        self.ser.clients.append(Game_data())
        self.assertTrue(len(self.ser.clients) == 1)
    def testRegistServer(self):
        game_data = self.ser.regist_server('game,1,0')
        self.assertTrue(isinstance(game_data, Game_data))
    def testMatchGame(self):
        c1 = Game_data()
        c2 = Game_data()
        self.ser.clients.append(c1)
        self.ser.clients.append(c2)
        self.ser.match_game()
        self.assertTrue(c1.client == c2)
        self.assertTrue(c2.client == c1)

class Game_data():
    def __init__(self, prefx = 'game', types = 1, info = '0'):
        self.prefx = prefx
        self.types = types
        self.info = info
        self.status = 0         # 0 is waitting, 1 is busy
        self.client = None      # 另一个客户端
class Game_dataTest(unittest.TestCase):
    def setUp(self):
        self.gd = Game_data()

if __name__ == '__main__':
    if DEBUG:
        unittest.main()
