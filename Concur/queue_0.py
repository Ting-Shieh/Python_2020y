"""
消息對列
聰過對象操作對列，滿足先進先出原則
"""

from multiprocessing import Queue, Process
from time import  sleep
from random import randint


# 創造消息對列


# 請求進程
def request(q):
    for i in range(10):
        sleep(0.5)
        t = (randint(1, 100), randint(1, 100))
        q.put(t)
        print("=============",i,"====================")


# 數據處理進程
def handle(q):
    while True:
        sleep(2)
        x, y = q.get()
        print("data hanle result x + y = ", x + y)

if __name__ == '__main__':
    q=Queue(5)
    p1 = Process(target=request, args=(q,))
    p2 = Process(target=handle, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()