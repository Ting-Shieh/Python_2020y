"""
自定義進程類
"""
from multiprocessing import Process
# 自定義進程類
class MyProcess(Process):
    def __init__(self, value):
        super().__init__()  # 加載父類init

    def f1(self):
        print("step1..")

    def f2(self):
        print("step2..")

    # 必定要調用
    def run(self):
        self.f1()
        self.f2()

if __name__ == '__main__':
    p = MyProcess(2)
    p.start()  # 執行run() => 作為一個子進程執行
    p.join()