"""
套接字屬性
"""
from socket import *

s =socket()
# print(dir(s))

# TODO 設置端口可以立即重用
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

s.bind(('192.168.10.100',4294))
s.listen(3)
conn, addr = s.accept()
print("地址類型: %s"%s.family)
print("套接字類型: %s"%s.type)
print("綁定地址: ",s.getsockname())
print("文件描述符: %s"%s.fileno())
# 使用連接套接字才能調用
print("獲取連接端的地址: ", conn.getpeername())
print("設置套接字選項: ",s.setsockopt())

conn.recv()  # 阻塞