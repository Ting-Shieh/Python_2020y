"""
開闢共享內存
=> 存取錢
Notice:
    共享內存只能有一個職

"""

from multiprocessing import Process, Value
import time
from random import randint



# 操作共享內存
def man(money):
    for i in range(30):
        time.sleep(0.2)
        money.value += randint(1,1000)

def girl(money):
    for i in range(30):
        time.sleep(0.15)
        money.value -= randint(100,800)


if __name__ == '__main__':
    # 創建共享內存
    money = Value('i', 5000)
    p1 = Process(target=man, args=(money,))
    p2 = Process(target=girl, args=(money,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('一個月的餘額: ',money.value)