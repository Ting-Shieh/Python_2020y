"""
同時創建多個子進程
"""
import os
import multiprocessing as mp
from time import sleep


def th1():
    sleep(3)
    print("吃飯!!")
    print('父=>',os.getppid(),' -- 子=>',os.getpid())

def th2():
    sleep(2)
    print("睡覺!!")
    print('父=>',os.getppid(),' -- 子=>',os.getpid())

def th3():
    sleep(4)
    print("打咚咚!!")
    print('父=>',os.getppid(),' -- 子=>',os.getpid())



if __name__ == '__main__':
    things = [th1, th2, th3]
    jobs = []
    for th in things:
        p = mp.Process(target = th)  # 列表存儲進程對象
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()