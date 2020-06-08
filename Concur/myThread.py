

from threading import Thread
from time import sleep,ctime


class MyClass(Thread):
    def __init__(self,target=None,args=(),kwargs={}):
        super().__init__()
        self.target= target
        self.args = args
        self.kwargs=kwargs

    def run(self):
        # * 傳參: 元祖按造位置傳參
        # ** 傳參: 字典按照關鍵字傳參
        self.target(*self.args, **self.kwargs)






def player(sec,song):
    for i in range(3):
        print("Playing %s : %s"%(song, ctime()))
        sleep(sec)

t = MyClass(target=player, args=(3,), kwargs={'song':"SHE"})
t.start()
t.join()