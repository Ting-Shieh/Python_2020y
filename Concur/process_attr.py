"""
進程函數船參數
"""
import os
import multiprocessing as mp
from time import sleep


# 帶參數進程
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I am %s"%name)
        print("I am working...")

if __name__ == '__main__':
    p = mp.Process(target=worker, args=(2,'Levi'), name="Test-1")  # 1.按照位置
    # p = mp.Process(target=worker, kwargs={'sec':2, 'name':'Levi'})  # 2.鍵值對傳參
    # p = mp.Process(target=worker, args=(2, ), kwargs={'name': 'Levi'}) # 3.鍵值對傳參
    p.daemon=True  # 子進程隨著父進程結束
    p.start()
    # sleep(5)
    print('Name: ', p.name)
    print('PID: ', p.pid)
    print('is alive: ', p.is_alive())
    # p.join() # join() 樂了阻塞等待子進程退出