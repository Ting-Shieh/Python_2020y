"""
http 請求響應
"""

from socket import *

# tcp 服務端
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)  # 端口立即重弄
s.bind(('127.0.0.1',4294))
s.listen(5)

c, addr =s.accept()
print("Connect from ", addr)
data = c.recv(4096)
print(data.decode())

html = """HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello World</h1>
    
"""
c.send(html.encode())
c.close()
s.close()