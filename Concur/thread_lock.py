"""
lock 演示
"""

from threading import Thread, Lock
a =  b = 0
lock = Lock()

def value():
    while True:

        lock.acquire()  # 上鎖
        print("線程 => 上鎖")
        if a != b:
            print("a = %d, b = %d" % (a,b))
        print("線程 => 解鎖")
        lock.release()  # 解鎖

t = Thread(target=value)
t.start()


while True:

    with lock:  # 上鎖
        print("主線程 => 上鎖")
        a += 1
        b += 1
        print("主線程 => 解鎖")
                # 解鎖

t.join()
