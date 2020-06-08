from exercise_process_thread.thread_test import *
import time
from multiprocessing import Process



if __name__ == '__main__':
    jobs = []
    tm = time.time()
    for i in range(10):
        # t = Process(target=count, args=(1, 1))
        t = Process(target=io)
        jobs.append(t)
        t.start()

    for i in jobs:
        i.join()
    print("multi Process CPU : ", time.time() -tm)