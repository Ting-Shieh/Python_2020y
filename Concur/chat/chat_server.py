
from socket import *
import os, sys


# 全局變量: 很多封裝模塊皆需要用或者有特定含意的變量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

# 存儲用戶{'name':address}
user = {}

def do_quit(s, name, text):
    """

    :param s:
    :param name:
    :param text:
    :return:
    """

    msg = "%s 退出群聊" % name
    for i in user:
        if i == name:
            s.sendto('EXIT'.encode(),user[i])
        else:
            s.sendto(msg.encode(), user[i])
    del user[name]

def do_chat(s, name, text):
    """
        處理聊天
    :return:
    :param s:
    :param name:
    :param text:
    """
    msg = "%s:%s" % (name, text)
    for i in user:
        # 不發送自己
        if i != name:
            s.sendto(msg.encode(),  user[i])


def do_login(s, name, addr):
    """
        處理用戶登入
    :param s:
    :param addr:
    :return:
    """
    if name in user or '管理員' in name:
        s.sendto("用戶名存在".encode(), addr)
        return
    else:
        s.sendto("OK".encode(), addr) # can login
    msg = "%s welcome to chat room " %name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr # add to dict
def do_request(s):
    """
        循環獲取客戶需求
    :param s:
    :return:
    """
    while True:
        data,addr = s.recvfrom(1024)  # L name
        tmp = data.decode().split(' ',2)
        # 根據不同的請求類型，執行不同的事件
        if tmp[0] == 'L':
            # 登入
            do_login(s, tmp[1], addr)
        elif tmp[0] == 'C':
            # chat
            do_chat(s,tmp[1],tmp[2])
        elif tmp[0] == 'Q':
            # 退出
            do_quit(s, tmp[1])





def main():
    """
        搭建網絡
        UDP 網絡
    :return:
    """
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid == 0:
        # 管理員消息發送處理
        while True:
            msg = input("管理員消息: ")
            msg = 'C 管理員 ' + msg
            s.sendto(msg.encode(), ADDR)

    else:
        do_request(s)  # 接收客戶端請求


if __name__ == '__main__':
    main()