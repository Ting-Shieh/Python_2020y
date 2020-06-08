"""
IO 多路復用
網路併發模型
重點過程
1.将关注的IO放入对应的监控类别列表
2.通过select函数进行监控
3.遍历select返回值列表，确定就绪IO事件
4.处理发生的IO事件
"""

from select import select
from socket import *
# help(select)
# 創造監聽套接字當作關注IO
s= socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 可立即重複使用
s.bind(('127.0.0.1',4294))
s.listen(3)

# TODO 設置關注列別
rlist = [s]  # 等待客戶端連接
wlist = []
xlist = []

# TODO 監控io發生
while True:
    rs, ws, xs = select(rlist, wlist, xlist, 3)
    for r in rs:  # TODO 遍历select返回值列表，确定就绪IO事件
        if r is s:
            # 有客戶端連接
            c, addr = r.accept()
            print("Connect From... ", addr)
            rlist.append(c) # 連接對象加入監控
        else:
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r) # 取消對它關注
                r.close()
                continue
            print(data)
            # r.send('OK'.encode())
            wlist.append(r)
    for w in ws:
        w.send('OK'.encode())
        wlist.remove(w)  # 不移除會一直重複發送

# f = open('./log.txt', mode='r')
#
# print("監控io~")
# rs, ws, xs =select([s],[s],[],3)
# print(rs)
# print(ws)
# print(xs)
