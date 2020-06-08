"""
發送一個文件
思路:
    循環讀取文件內容，發送

"""


from socket import *
filename = './Data/marvel.jpg'

s = socket()
s.connect(('127.0.0.1', 4294))


f = open(filename, mode = 'rb')

while True:
    # 邊讀邊發
    data =f.read(1024)
    if not data:  # 讀到文件結尾
        break
    s.send(data)

f.close()
s.close()