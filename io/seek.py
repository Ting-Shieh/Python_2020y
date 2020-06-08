import  os

file_name = "./Data/io_demo.txt"
file_name2 = "./Data/test2.txt"
f = open(file_name, mode ='a+',encoding='utf-8')
# f.write("獲取文件偏移量練習=>tell()\n")
# print("文件偏移量: ", f.tell())
# print("文件描述符: ", f.fileno())

print("獲取文件大小: ", os.path.getsize(file_name))
print("查看文件列表(當前): ", os.listdir('.'))
print("查看文件是否存在: ", os.path.exists(file_name))
print("判断文件类型: ", os.path.isfile(file_name))
print("删除文件: ", os.remove(file_name2))


