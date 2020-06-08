
from multiprocessing import Pool, Queue, Process
import os


size_list = []
def get_total_size(file_list,old_file):
    total_size=0
    for f in file_list:
        total_size += os.path.getsize(old_file+f)

    return total_size



def copy_file(file_name, old_file, new_file):
    fr = open(old_file+file_name, mode='rb')
    fw = open(new_file+file_name, mode='wb')
    print(file_name)
    while True:
        data = fr.read(1024)  # 1k
        if not data:
            break
        fw.write(data)  # 寫入的字節數
        # q.put(n)  # 放入消息對列中
    fr.close()
    fw.close()

def put_n(size_list,q):
    for n in size_list:
        q.put(n,block=True)

def show_progress(total_size,q):
    copy_size = 0
    while copy_size<total_size:
        print("show...")
        copy_size += q.get(timeout=3)
        print("copy progressbar: %.2f%%", (copy_size/total_size*100))

def copy_file_q(file_name, old_file, new_file):

    fr = open(old_file+file_name, mode='rb')
    fw = open(new_file+file_name, mode='wb')
    # print(file_name)
    while True:
        data = fr.read(1024)  # 1k
        if not data:
            break
        n = fw.write(data)  # 寫入的字節數
        print(n)
        size_list.append(n)


    fr.close()
    fw.close()




if __name__ == '__main__':

    path = './'
    dir = 'data'
    old_file = path+dir+'/'
    new_file = path+dir+"-copy/"
    os.mkdir(new_file)
    file_list = os.listdir(old_file)
    print("計算總大小中...")
    total_size = get_total_size(file_list,old_file)
    print("總大小 = %d "% (total_size))

    # 創建消息對列
    q = Queue(3)
    pool = Pool(4)

    # for file_name in file_list:
    #     pool.apply_async(func=copy_file, args=(file_name, old_file, new_file))

    for file_name in file_list:
        pool.apply_async(func=copy_file_q,args=(file_name, old_file, new_file))

    print(size_list)

    # 關閉進程池
    pool.close()
    # copy_size = 0
    # while copy_size < total_size:
    #     print("show...")
    #     copy_size += q.get()
    #     print("copy progressbar: %.2f%%", (copy_size / total_size * 100))
    # show_progress(total_size, q)
    p1 = Process(target=put_n, args=(size_list,q))
    p2 = Process(target=show_progress, args=(total_size,q))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # 回收進程池
    pool.join()