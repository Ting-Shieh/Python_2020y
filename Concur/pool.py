"""
進程池

"""

from multiprocessing import Pool
from time import sleep, ctime


# 進程池事件
def worker(msg):
    sleep(2)
    print(ctime(), '--', msg)

if __name__ == '__main__':

    # 創建進程池
    pool = Pool(4)

    # 添加時間
    for i in range(10):
        msg = "Ting %d" % i
        pool.apply_async(func=worker, args=(msg,))

    # 關閉進程池
    pool.close()
    # 回收進程池
    pool.join()
