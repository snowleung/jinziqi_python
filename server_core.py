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

class Core_TCPTest(unittest.TestCase):
    def setUp(self):
        self.ser = Core_TCP()
    def testClientList(self):
        self.assertTrue(len(self.ser.clients) == 0)
        self.ser.clients.append(Game_data())
        self.assertTrue(len(self.ser.clients) == 1)

class Game_data():
    def __init__(self):
        self.prefx = 'game'
        self.types = 1
        self.info = '0'
class Game_dataTest(unittest.TestCase):
    def setUp(self):
        self.gd = Game_data()

if __name__ == '__main__':
    if DEBUG:
        unittest.main()
