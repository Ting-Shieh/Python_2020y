"""
信號亮控制
"""

from multiprocessing import Process, Semaphore
import os, time
from random import randint

def handle(sem):
    sem.acquire()  # 執行任務必須消耗一個信號量
    print("開始執行任務: ", os.getpid())
    time.sleep(2)
    print('執行任務結束: ', os.getpid())
    sem.release()  # 增加一個訊號量


if __name__ == '__main__':
    # 創建訊號量
    sem = Semaphore(3)
    for i in range(5):
        p = Process(target=handle, args=(sem,))
        p.start()