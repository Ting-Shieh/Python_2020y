"""
線程屬性
"""

from threading import Thread
from time import sleep,time

def fun(sec,name):
    print("%s分支線程開始執行"%name)
    sleep(sec)
    print("%s分支線程執行完畢"%name)


t =Thread(target=fun, args=(2,),kwargs={'name':'Test-Thread'},daemon=True)
print('Name:',t.getName())
t.setName('Test-Thread2')
print('after set Name:',t.getName())
print('=========================')
print('is thread alive:',t.is_alive())
t.start()
print('after start() is thread alive:',t.is_alive())
print('=========================')