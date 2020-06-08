"""
利用 fork 進行多進程併發

1. 創建 監聽套接字
2. 循環等待客戶端連接
3. 客戶端連接創建新的進程為客戶端服務
4. 原進程繼續等待其他客戶端連接
5. 客戶端退出，對應進程消失。
"""

from socket import *
import os
import  signal
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
s.bind()
s.listen(5)  # window 底下不管用

# 處理殭屍
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("Listen the port 8888...")

# 2. 循環等待客戶端連接
while True:
    try:
        conn, addr = s.accept()
        print("Connect From ", addr)
    except KeyboardInterrupt as e:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 3. 客戶端連接創建新的進程為客戶端服務
    pid = os.fork()
    if pid == 0:
        s.close()
        handle(conn)  # 子進程與客戶端交互
        os._exit(0)  # 客戶端交互結束後，子進程結束
    else:
        # pid < 0 or pid > 0:
        # 1.創建進程出錯
        # 2.繼續等待其他客戶端連接
        conn.close()