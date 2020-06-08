from exercise_process_thread.thread_test import *
import time
import threading

jobs = []
tm = time.time()
for i in range(10):
    # t = threading.Thread(target=count, args=(1,1))
    t = threading.Thread(target=io)
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()

print("multi Thread CPU : ", time.time() -tm)