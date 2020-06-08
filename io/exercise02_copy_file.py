# fr = open('./Data/marvel.jpg',mode = 'rb')
# fw = open('./Data/marvel_copy.jpg',mode = 'wb')
# fw.write(fr.read())

filename = input("文件:")
fr = open('./Data/'+filename+'.jpg', mode = 'rb')
fw = open("copy_"+filename, mode = 'wb')

""" 
    防止讀取文件過大
"""
while True:
    data = fr.read(1024)
    if not data:
        break
    fw.write(data)

fr.close()
fw.close()
