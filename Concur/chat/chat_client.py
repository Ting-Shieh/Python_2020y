"""
Chat room 客戶端
發送請求，展示結果
"""

from socket import *
import os, sys

# 服務器地址
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)

def recv_msg(s):
    """
        接收消息
    :return:
    """
    while True:
        data, addr = s.recvfrom(4096)
        # 收到exit 接收進程結束
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+'\n>>',end='')


def send_msg(s, name):
    """
        發送消息
    :return:
    """
    while True:
        try:
            text = input(">> ")
        except (KeyboardInterrupt,SyntaxError):
            text = 'quit'
        if text.strip() == 'quit':
            msg = "Q "+name
            s.sendto(msg.encode(), ADDR)
            sys,exit("退出聊天室")
        msg = "C %s %s" % (name, text)
        s.sendto(msg.encode(), ADDR)

def main():
    """
        搭建網絡
        UDP 網絡
    :return:
    """
    s = socket(AF_INET, SOCK_DGRAM)
    # 進入聊天室
    while True:
        name = input("請輸入稱號: ")
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)
        # 接受反饋
        data, addr = s.recvfrom(128)
        if data == b'OK':
            print("您已進入聊天室!")
            break
        else:
            print(data.decode())

        # 以實已經進入聊天室
        pid = os.fork()
        if pid < 0:
            sys.exit("Error!!")
        elif pid == 0:
            # 子進程
            send_msg(s,name)
        else:
            # 父進程
            recv_msg(s)


if __name__ == '__main__':
    main()
