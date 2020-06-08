from exercise_process_thread.thread_test import *
import time



tm = time.time()

for i in range(10):
    # count(1,1)
    io()
print("no thread CPU : ", time.time() - tm)