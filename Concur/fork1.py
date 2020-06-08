"""
 module 'os' has no attribute 'fork'
 os.fork() 不能在window上使用
"""


import os
pid = os.fork()
if pid < 0:
    print("Create process failed!")
elif pid == 0:
    # 子進程 執行部分
    print("The new process")
else:
    # 父進程 執行部分
    print("The old process")

print("Fork test over!!")