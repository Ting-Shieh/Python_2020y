
"""
udp
從客戶端輸入 學號 姓名 年紀 分數
將訊息發送給服務端
在服務端寫入到一個無見裡面
每一個學生訊息一行

===> 客戶端
"""
import struct
from socket import *


server_addr = ('127.0.0.1', 8888)


class Student:
    def __init__(self,id=None, name=None, age=None, score=None):
        self.id = id
        self.name = name
        self.age = age
        self.score = score



class SetStruct:
    def __init__(self):
        self.st = struct.Struct("i16sif")
    def set_struct(self,stu=None):
        """
        將數據打包
        :param stu: 學生
        :return:
        """
        if stu:
           return self.st.pack(stu.id, stu.name.encode(), stu.age, stu.score)

    def get_struct(self, data):
        """
            解包
        :param stu:
        :return: 元祖型態
        """
        return self.stu.unpack(data)

# 創建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 綁定地址
sockfd.bind(server_addr)
print("UDP started...")
# 循環收發消息
while True:
    print("============================")
    id = int(input("id: "))
    name = input("name: ")
    age = int(input("age: "))
    score = int(input("score: "))
    stu = Student(id,name, age, score)
    # TODO 將數據打包  發送給服務端
    sockfd.sendto(SetStruct().set_struct(stu), server_addr)

sockfd.close()