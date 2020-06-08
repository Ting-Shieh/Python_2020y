"""
multiprocessing
1. 編寫進程執行函數
2. 創建進程對象
3. 啟動進程
4. 回收進程
"""

import multiprocessing as mp
from time import sleep

# 進程函數
def fun():
    print("start one process...")
    sleep(3)
    print('process is over.')

if __name__ == '__main__':  #必須放這段代碼，不然會Error
    """
    等同以下
    pid = os.fork()
    if pid == 0:
        # 子進程
        fun()
    else: 
        # 父進程
        os.wait() 
    """
    # 創建進程對象
    p = mp.Process(target=fun)
    # 啟動進程
    p.start()
    # 回收進程
    p.join()