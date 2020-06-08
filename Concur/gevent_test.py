import gevent
from gevent import monkey
monkey.patch_time()

from time import sleep

#協成函數
def fun1(a,b):
    print("執行1 a=%d,b=%d"%(a,b))
    sleep(3)
    print("結束fun1")

def fun2(a,b):
    print("執行2 a=%d,b=%d"%(a,b))
    sleep(2)
    print("結束fun2")

# 生成協成對象
g1 = gevent.spawn(fun1,1,2)
g2 = gevent.spawn(fun2,1,2)
gevent.joinall([g1,g2])