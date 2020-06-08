
# 計算 密集
def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

# io 密集
def io():
    write()
    read()


def write():
    f = open('./data/file_test.txt', mode='w')
    for i in range(1700000):
        f.write('Hi Ting _ %d \n'%i)
    f.close()
def read():
    f = open('./data/file_test.txt', mode='r')
    lines = f.readlines()
    f.close()
