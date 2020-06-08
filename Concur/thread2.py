"""
帶參數的線程函數
"""

from threading import Thread
from time import sleep,time

# 帶參數的線程函數
def fun(sec,name):
    print("%s分支線程開始執行"%name)
    sleep(sec)
    print("%s分支線程執行完畢"%name)

# 創建多線程
jobs=[]
for i in range(5):
    t =Thread(target=fun, args=(2,),kwargs={'name':'T-%d'%i})
    jobs.append(t)
    t.start()

for j in jobs:
    j.join()
