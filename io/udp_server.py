"""

"""

from socket import *

# 創建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 綁定地址
server_addr = ('192.168.10.100', 4294)
sockfd.bind(server_addr)
# 與 tcp 不同，不需要任何連接
print("UDP started...")
# 循環收發消息
# TODO 因為沒有一職連接，所以當客戶端退出時，也不會報錯
# TODO 超過1024字節後，及丟失
while True:
    data, addr = sockfd.recvfrom(3)
    print("Msg From %s: %s" %(addr, data.decode()))
    sockfd.sendto(b"Thanks!", addr)

# 關閉套接字
sockfd.close()