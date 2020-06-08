"""
多進程併發
1. 創建 監聽套接字
2. 循環等待客戶端連接
3. 客戶端連接創建進程為客戶端服務
4. 父進程繼續等待其他客戶端連接
5. 客戶端退出，對應子進程消失。
"""
import signal, sys
from multiprocessing import Process
from socket import *




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

# 處理殭屍
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

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

    # 3. 客戶端連接創建新的進程為客戶端服務
    p = Process(target=handle, args=(conn,))
    p.daemon = True
    p.start()
