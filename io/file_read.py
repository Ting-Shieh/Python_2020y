file_name = "./Data/io_demo.txt"
f = open(file_name, mode ='a+')


# 打開文件
try:
    # f = open(file_name, mode ='r')  # mode='r': 只讀方式
    # f = open('demo.py', mode = 'w')  # mode = 'w':　不存在則創建，存在則清空
    # f = open('demo.py', mode = 'a')    # mode = 'a':　不存在則創建，存在則追加
    f = open(file_name, mode='r', encoding='utf8')

    """
    read()
    """
    # while True:
    #     data = f.read(3)
    #     if not data:
    #         break
    #     print(data)

    """
    # print("----------readline----讀取一行--------")
    """
    # data_readline = f.readline()
    # print('1-', data_readline)
    # data_readline = f.readline()
    # print('2-',data_readline)


    """
    # print("----------readlines----讀取內容到一個列表--------")
    """
    # data_readlines = f.readlines()
    # print('讀取內容到一個列表-', data_readlines)



    # 文件對象具可迭代屬性
    for line in f:
        print(line)

except Exception as e:
    print(e)
# 讀寫文件

# 關閉文件

f.close()