tuple01 = (4,5,66,7,2)
for item in tuple01:
    print(item)
print("="*30)
iterator = tuple01.__iter__()
while True:
    # 如果迭代器中沒有可以繼續 __next__ 值
    # 會拋出停止迭代 的異常
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
print("="*30)
dict01 = {"A1":101,'B2':102,'C3':103}
dict_iterator = dict01.__iter__()
while True:
    try:
        key = dict_iterator.__next__()
        print(key,dict01[key])
    except StopIteration:
        break

