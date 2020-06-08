file_name = "./Data/io_demo.txt"

f = open(file_name, mode ='a')

while True:
    data = input(">>")
    if not data:
        break
    f.write(data+'\n')
    f.flush()

f.close()