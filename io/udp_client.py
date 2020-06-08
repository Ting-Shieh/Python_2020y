"""


"""

from socket import *
Addr = ('192.168.10.100', 4294)  # 全域變量
# 創建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 循環收發消息
while True:
    data = input("Msg:")
    if not data:
        break
    sockfd.sendto(data.encode(),Addr)
    msg, addr = sockfd.recvfrom(1024)
    print("From server:", msg.decode())

# 關閉套接字
sockfd.close()