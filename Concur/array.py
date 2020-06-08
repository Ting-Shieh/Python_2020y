"""
存放一組數據
"""
import os
from multiprocessing import Process, Array
import time
from random import randint


def fun(shm):
    # 迭代獲取共享內存值
    for i in shm:
        print(i)
    shm[0]='t'.encode()



if __name__ == '__main__':

    # 共享內存，初始數據 [1,2,3,4,5]
    # shm = Array('i',4)# 初始[0,0,0,0]
    shm = Array('c', b'Ting')
    p = Process(target=fun, args=(shm,))
    p.start()
    p.join()
    # 用於 'i'
    # for i in shm:
    #     print(i)
    print(shm.value)  # 用於打印共享內存字節串



