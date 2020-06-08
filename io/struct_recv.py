"""
udp
從客戶端輸入 學號 姓名 年紀 分數
將訊息發送給服務端
在服務端寫入到一個無見裡面
美醫學生訊息站一行

===> 服務端
"""
import struct
from socket import *


server_addr = ('127.0.0.1', 4294)


class SetStruct:
    def __init__(self):
        self.st = struct.Struct("i16sif")

    def get_struct(self, data):
        """
            解包
        :param stu:
        :return: 元祖型態
        """
        return self.stu.unpack(data)

class WriteFileTool:
    def __init__(self):
        self.file_name = "./Data/students.txt"
        self.f = open(self.file_name, mode='a+', encoding='utf8')

    def write_stu(self,data_tuple):

        info = "%d--%-10s--%d--%.1f\n" % data_tuple
        self.f.write(info)
        self.f.flush()

        return "Writed id: %d into file" % data_tuple[0]

    def close_file(self):
        return self.f.close()

# 與客戶端格式一致
# 套用已打包好的
# st = struct.Struct("il6sif")

tool = WriteFileTool()

# 創建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 綁定地址
sockfd.bind(server_addr)

while True:

    data, addr = sockfd.recvfrom(1024)
    date_tuple = SetStruct().SetStruct.get_struct(data)
    res = tool.write_stu(date_tuple)
    print(res)

tool.close_file()
sockfd.close()