"""
接受一個文件
接收一個文件內容，將其寫入到一個文件裡
"""

from socket import *

s = socket()
s.bind(('127.0.0.1',4294))
s.listen(3)

c,addr = s.accept()
print("Connet from", addr)

# 打開文件
filename = './Data/test.jpg'
f = open(filename, mode = 'wb')

# 循環接收內容，寫入文件
while True:
  data = c.recv(1024)
  if not data:
      break
  f.write(data)

f.close()
c.close()
s.close()