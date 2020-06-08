"""
poll io多錄用
【1】 创建套接字
【2】 将套接字register
【3】 创建查找字典，并维护
【4】 循环监控IO发生
【5】 处理发生的IO
"""

from select import *
from socket import *
import select
# 創造監聽套接字當作關注IO


s= socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 可立即重複使用
s.bind(('127.0.0.1',4294))
s.listen(3)

fdmap = {s.fileno():s}
# TODO  創建 poll對象 設置關注列別
p = select.poll()
p.register(s.fileno(), select.POLLIN|select.POLLERR)

# TODO 監控io發生
while True:
    events = p.poll()
    for fd, event in events:
        if fd ==s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect From... ", addr)

            p.register(c, select.POLLIN|select.POLLERR)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data)
            p.register(fd, select.POLLERR)
            # fdmap[fd].send('OK'.encode())
        elif event & select.POLLOUT:
            fdmap[fd].send('OK'.encode())
            p.register(fd, select.POLLERR)