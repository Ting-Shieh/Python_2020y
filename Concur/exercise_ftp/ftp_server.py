"""
ftp 文件服務器 服務端
多進程/多線程併發 socket練習
"""
import os
import sys
from  time import time, sleep
from socket import *
from threading import Thread
HOST = '0.0.0.0'
PORT = 4294
ADDR = (HOST, PORT)
FTP = r'C:\\Users\\User\\Desktop\\Online Courses\\'  # 文件庫位置 # 資料夾不屬於文件


# 實現具體功能
# 自定義線程類
class FtpServer(Thread):
    """
    查看文件列表, 上傳, 下載, 退出
    """
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd

    def do_put(self, filename):
        """
            接收上傳文件
        :param filename:
        :return:
        """
        if os.path.exists(FTP+filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send("OK".encode())
        # 接收上傳文件
        f= open(FTP+filename,mode='wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    def do_get(self,filename):
        """
            下載文件
        :param filename:
        :return:
        """
        # 判斷是否存在
        try:
            f = open(FTP+filename, mode='rb')
        except Exception :
            # 文件不存在
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send("OK".encode())
            # 發文件過程中，不用擔心沾包
            # 沾包容易出現在連續發送的情況下
            sleep(0.1)
        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send('##'.encode())
                break
            self.connfd.send(data)

    def do_list(self):
        """
            查看文件列表
        :return:
        """
        files = os.listdir(FTP)
        if not files: # 表示為空
            self.connfd.send("充值VIP!!".encode())
            return
        else:
            self.connfd.send('OK'.encode())
            sleep(0.1)

        # 法2: 一次發送
        filelist = ""
        for file in files:
            if file[0] != '.' and os.path.isfile(FTP+file):
                filelist += file + '\n'

        self.connfd.send(filelist.encode())


        # 法1
        # for file in files:
        #     #  不為隱藏文件        為普通文件
        #     if file[0] != '.' and os.path.isfile(FTP+file):
        #         sleep(0.1)  # 防止沾黏
        #         self.connfd.send(file.encode())
        # sleep(0.1)
        # self.connfd.send('##'.encode())

    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            # 判斷請求類型
            if not data or data == 'Q':
                return  # 線程結束
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)
            print(data)
            self.connfd.send('OK'.encode())
        self.connfd.close()



# 搭建網絡併發模型
def main():
    # 創建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    print("Listen the port 4294")
    # 循環等待客戶端連接
    while True:
        try:
            conn, addr = s.accept()
            print("Connect From ", addr)
        except KeyboardInterrupt as e:
            sys.exit("Ftp Server Exit")
        except Exception as e:
            print(e)
            continue

        # 客戶端連接創建新的線程為客戶端服務
        t = FtpServer(conn)
        t.setDaemon((True)) # 設置主線程退出時，分支線程一起退出
        t.start()


if __name__ == '__main__':
    main()