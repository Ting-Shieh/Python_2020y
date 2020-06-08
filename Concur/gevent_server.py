import gevent
from gevent import monkey
monkey.patch_all()
from socket import *


def handel(c):

    while True:
        data = c.recv(1024).decode()
        if not data:
            return
        print(data)
        c.send('OK'.encode())

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
s.bind(('127.0.0.1',4294))
s.listen(5)

while True:
    c,addr = s.accept()
    print("Connect From ...", addr)
    gevent.spawn(handel,c)
