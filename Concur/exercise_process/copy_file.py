from multiprocessing import Process
import os

filename = './tesla.jpg'
size = os.path.getsize(filename)  # 獲取文件大小
fr = open(filename, mode='rb')  # 父進程打開 文件
# print(fr.fileno())


# 複製上半部
def file_top():
    # fr = open(filename, mode='rb')
    print('file_top no:', fr.fileno())
    fw = open('copy_tesla_top.jpg', mode='wb')
    fw.write(fr.read(size//2))
    fr.close()
    fw.close()
# 複製下半部
def file_bottom():
    # fr = open(filename, mode='rb')
    print('file_bottom no:', fr.fileno())
    fw = open('copy_tesla_bottom.jpg', mode='wb')
    fr.seek(size//2)  # 文件偏移量移至到中間
    fw.write(fr.read())  # 一直讀到結尾
    fr.close()
    fw.close()

if __name__ == '__main__':

    # p1 = Process(target=file_top, args=(fr,))
    # p2 = Process(target=file_bottom, args=(fr,))
    print(fr.fileno())
    p1 = Process(target=file_top)
    p2 = Process(target=file_bottom)

    p1.start()
    p2.start()
    p1.join()
    p2.join()