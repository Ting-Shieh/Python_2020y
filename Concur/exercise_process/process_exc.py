"""
球100000以內所有質數之合
分別用
1. 單進程  4進程  10進程 完成
2. 計入每種情況的執行時間，通過裝飾氣紀錄時間
"""
from timeit import timeit
from multiprocessing import Process




def isPrime(n):
    """
        判斷是否為質數
    :param n:
    :return:
    """
    if n<=1:
        return False
    for i in range(2,int(2)):
        if n % i == 0:  # 不是質數
            return False
    return True  # 是質數

@timeit
def no_multi_process():
    """
        單進程
    :return:
    """
    prime = []
    for i in range(1, 1000001):
        if isPrime(i):
            prime.append(i)

    sum(prime)


class Prime(Process):
    def __init__(self, prime, begin, end):
        super().__init__()
        self.prime =prime  # 裝質數的列表
        self.begin =begin  # 開始位
        self.end = end     # 結束位


    def run(self):
        """

        :return:
        """
        for i in range(self.begin, self.end):
            if isPrime(i):
                self.prime.append(i)
        sum(self.prime)

@timeit
def use_4_process():
    prime = []
    jobs = []
    for i in range(1, 1000001, 25000):
        p = Prime(prime,i, i+25000)
        jobs.append(p)
        p.start()

     # 回收進程
    [j.join() for j in jobs]


@timeit
def use_10_process():
    prime = []
    jobs = []
    for i in range(1, 1000001, 10000):
        p = Prime(prime,i, i+10000)
        jobs.append(p)
        p.start()

     # 回收進程
    [j.join() for j in jobs]

if __name__ == '__main__':
    # use_4_process()
    use_10_process()