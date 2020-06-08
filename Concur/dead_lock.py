"""
死鎖模擬
模擬銀行帳戶取帳款
"""

from threading import Thread, Lock
from time import sleep

class Acount:
    def __init__(self,_id, blance, lock):
        self._id = _id
        self.blance = blance
        self.lock = lock

    def withdraw(self,amount):
        """
            取錢
        :param amount:
        :return:
        """
        self.blance -= amount

    def deposit(self,amount):
        """
            存錢
        :param amount:
        :return:
        """
        self.blance += amount


    def get_balance(self):
        """
            查看餘額
        :return:
        """
        return self.blance


def transfer(from_, to_, amount):
    """
        轉帳 帳戶金額變動需要先上鎖
    :return:
    """
    if from_.lock.acquire():
        from_.withdraw(amount)
        sleep(0.1)
        if to_.lock.acquire():
            to_.deposit(amount)
            to_.lock.release()
        from_.lock.release()
    print("%s 給 %s 轉了 %d 元" % (from_._id, to_._id, amount))

# 生成 兩個帳戶
Tom = Acount('Tom', 12000, Lock())
Abby = Acount('Abby', 9000, Lock())

# 模擬轉帳

t1 = Thread(target=transfer, args=(Tom, Abby, 4000))
t2 = Thread(target=transfer, args=(Abby, Tom, 2500))
t1.start()
t2.start()
t1.join()
t2.join()

print("Tom: ",Tom.get_balance())
print("Abby: ",Abby.get_balance())