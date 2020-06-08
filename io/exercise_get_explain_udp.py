"""
使用udp完成，在客戶端循環的輸入單詞，得到單詞解釋，輸入 enter ，退出查詢，可以滿足同時啟動多個客戶端一起查詢
"""
from socket import *


server_addr = ('192.168.10.100', 4294)
file_name = "./Data/dict.txt"
f = open(file_name, mode='r', encoding='utf8')

def get_explain(word):
    for line in f:
        target = line.split(" ")[0]
        # 遍歷的單字已經大於目標，表示找不到
        if target > word:
            break
        elif word == target:
            f.close()
            return line.split(".")[-1]

    # 考慮輸入的單字特別大的防呆
    else:
        return "沒找到該單字"


# 創建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 綁定地址
sockfd.bind(server_addr)
print("UDP started...")
# 循環收發消息
while True:
    data, addr = sockfd.recvfrom(1024)
    print("Msg From %s: %s" %(addr, data.decode()))
    # res = get_explain(data.decode())
    sent_str = "This is answer ==> "
    sent_str += get_explain(data.decode())
    sockfd.sendto(sent_str.encode(),addr)