"""
套接字
非阻塞IO
"""

from socket import *
from time import sleep, ctime
f = open('./log.txt', mode='a', encoding='utf8') # 日誌文件



s = socket()
s.bind(('0.0.0.0',4294))
s.listen(5)

# # TODO 設置套接字非阻塞
# s.setblocking(False)

# TODO 設置超時時間
s.settimeout(3)

while True:
    try:
        c, addr = s.accept()
        print("Connect from..",addr)
    except BlockingIOError as e:
        sleep(2)
        f.write(str(ctime())+" : "+str(e)+'\n')
        f.flush()
    except timeout as e:
        sleep(2)
        f.write(str(ctime()) + " : " + str(e) + '\n')
        f.flush()
    else:
        data = c.recv(1024)
        print(data.decode())
