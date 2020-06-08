"""

"""
import os
import time

file_name = "./Data/log.txt"
f = open(file_name, mode ='a+')
f.seek(0)  # 將文件篇一輛放置最一開始

n = len(f.readlines())

while True:
     n += 1
     time.sleep(1)
     s = "%d. %s \n" % (n, time.ctime())
     f.write(s)
     f.flush()