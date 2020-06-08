"""
多線程併發
1. 創建 監聽套接字
2. 循環等待客戶端連接
3. 客戶端連接創建新的線程為客戶端服務
4. 主線程繼續等待其他客戶端連接
5. 客戶端退出，對應分支消失。
"""

from socket import *
import os
import sys
from threading import  Thread


# 全局變量: 多封裝皆需要
Host = '0.0.0.0'
PORT = 8888
ADDR = (Host, PORT)


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send('OK'.encode())
    c.close()

# 1. 創建 監聽套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)  # window 底下不管用


print("Listen the port 8888...")

# 2. 循環等待客戶端連接
while True:
    try:
        conn, addr = s.accept()
        print("Connect From ", addr)
    except KeyboardInterrupt as e:
        sys.exit("SERVER EXIT")
    except Exception as e:
        print(e)
        continue

    # 3. 客戶端連接創建新的線程為客戶端服務
    t = Thread(target=handle, args=(conn,))
    t.setDaemon(True)  # 設置主線程退出時，分支線程一起退出
    t.start()
