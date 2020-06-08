import time

# for item in time.localtime():
#     print(item)

print(time.localtime(time.time()))


print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# 將字串轉為時間元祖
print(time.strptime("2020/04/29 11:31:30","%Y/%m/%d %H:%M:%S"))