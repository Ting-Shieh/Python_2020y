"""
Thread Step
1.封裝線程函數
2.創建線程對象
3.啟動線程
4.回收線程

主線程和分支線程隸屬於同一進程!!!!

"""

import threading
import os
from time import sleep,time
sstart_time = time()

a = 1
# 封裝線程函數
def music():
    global a
    print('a= ',a)
    a = 10000
    for i in range(3):
        strart_time = time()
        sleep(2)
        print(os.getpid(),"...Maroon5..分支線程播放...",time()-strart_time)

# 創建線程對象
t = threading.Thread(target=music)

# 啟動線程
t.start()

# 主線程
for i in range(4):
    print("啟動sleep ==>")
    sleep(1)
    print(os.getpid(),"...SHE..主線程播放...")

# 回收線程
t.join()
print("a= ",a)
print("Total Time:",time()-sstart_time)