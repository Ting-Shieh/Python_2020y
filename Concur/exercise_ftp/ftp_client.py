"""
ftp 文件服務器 客戶端

"""

from socket import *
import sys
from  time import time, sleep


HOST = '127.0.0.1'
PORT = 4294
ADDR = (HOST, PORT)

class FtpClient:
    """
    實現具體功能請求
    """
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        """
            查看列表
        :return:
        """
        self.sockfd.send('L'.encode())
        # 提醒服務器要發請求了，等待回復
        # 確認是否有文件列表
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(1024).decode()
            print(data)

            # 法1
            # while True:
            #     data = self.sockfd.recv(128).decode()
            #     if data == '##':
            #         break
            #     print(data)
        else:
            print(data)  # 不可以查看的原因

    def do_get(self, filename):
        """

        :param filename: 文件名
        :return:
        """
        # 發送請求
        self.sockfd.send(('G '+filename).encode())
        # 等待回復
        data = self.sockfd.recv(128).decode()
        # 接收文件
        if data == 'OK':
            f = open(filename, mode='wb')
            # 循環接收內容寫入文件
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                f.write(data)
            f.close()
        else:
            print(data)


    def do_put(self, filename):
        """
            上傳文件
        :param filename:
        :return:
        """
        # 判斷是否存在
        try:
            f = open(filename, mode='rb')
        except Exception:
            # 文件不存在
            print(" File do not exits.")
            return
        # 發送請求
        if '/' in filename:
            filename = filename.split('/')[-1]

        self.sockfd.send(('P '+filename).encode())
        # 等待回復(是否已經存在)
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
                f.close()
        else:
            print(data)


    def do_quit(self):
        """
            退出功能
        :return:
        """
        self.sockfd.send('Q'.encode())
        self.sockfd.close()
        sys.exit("~~謝謝使用~~")




# 網絡搭建，終端輸入命令選項
def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return
    # 實例化對象
    ftp = FtpClient(sockfd)
    # 循環發起請求
    while True:
        print('\n============== Command =================')
        print("*****           list               ******")
        print("*****          get file            ******")
        print("*****          put file            ******")
        print("*****           quit               ******")
        print('================ Command =================')
        cmd = input("Command: ")
        if cmd.strip() == 'list':
            ftp.do_list()

        elif cmd.strip() == 'quit':
            ftp.do_quit()

        elif cmd.strip()[:3] == 'get':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_get(filename) # 發起請求，接收回復，獲取文件
        elif cmd.strip()[:3] == 'put':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_put(filename) # 發起請求，接收回復，獲取文件
        else:
            print("請輸入正確命令!!")



if __name__ == '__main__':
    main()