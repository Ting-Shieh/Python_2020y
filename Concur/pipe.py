"""
管道通信
注意:
    管道對象需要在父進程中創建，子進程從父進程中獲取
"""

from multiprocessing import Pipe, Process



def app1(fd1):
    print("start app1 to login,and u can use app2...")
    print("send request to app2...")
    fd1.send("app1 need: User Name and Pic")  # 寫管道
    data = fd1.recv()
    print("Login Success!!", data)

def app2(fd2):
    data = fd2.recv()   # 讀管道
    print("app1 send request ===> ", data)
    fd2.send({'User Name':'Ting', 'Pic-Image':'有'})

if __name__ == '__main__':
    # 創建管道
    # False: 單向管道  ===> fd1->recv, fd2->send
    # 不要在一個進程中，同時使用 fd1, fd2
    fd1, fd2 = Pipe()
    p1 = Process(target=app1, args=(fd1,))
    p2 = Process(target=app2, args=(fd2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()