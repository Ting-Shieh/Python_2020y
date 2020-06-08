"""
tcp 套接字客戶端流程
注意:
    和服務端配合使用相同的套接字
如何測試:
    在終端機上: telnet  ipv4  port
"""

import socket


# 創接 tcp 套接字對象
sockfd = socket.socket()


# 連接服務器 與服務端配合
server_addr = ('192.168.10.100', 4294)   # 服務端地址
sockfd.connect(server_addr)
# 先發後收
while True:
    msg = input("Msg: ")
    if not msg:
        break
    sockfd.send(msg.encode())   # 發送一定要字節串
    # if msg == "Q":
    #         break
    data = sockfd.recv(1024)
    print('From Server %s' % data.decode())

# 關閉套接字
sockfd.close()