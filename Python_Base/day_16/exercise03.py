# 定義函數，獲取列表中所有偶數
# 將所有滿足條件的數存入新列表，生成器方式(yield)
list01 = [4,54,65,6,76,87,9]
print("=======練習1=======")
# 1.傳統
def get_even(obj):
    new_list = []
    for num in obj:
        if num%2 ==0:
            new_list.append(num)
    return new_list

for item in get_even(list01):
    print(item)

# 2. 生成器方式(yield) =>省內存
def get_even2(obj):
    for num in obj:
        if num%2 ==0:
            yield num

for item in get_even2(list01):
    print(item)

print("=======練習2=======")
# 1.傳統
def get_bigger_than_10_v1(obj):
    new_list = []
    for item in obj:
        if item >= 10:
            new_list.append(item)
    return new_list
print("=======練習2-傳統=======")
for item in get_bigger_than_10_v1(list01):
    print(item)

# 2. 生成器方式(yield) =>省內存
def get_bigger_than_10_v2(obj):
    for item in obj:
        if item >= 10:
            yield item
print("=======練習2-enumerate=======")
for item in get_bigger_than_10_v2(list01):
    print(item)
list02 = ['A',"B","C",'A1',"B1","C1"]
print("=======練習3-傳統enumerate=======")
for item in enumerate(list02):
    print(item)
print("=======練習3-生成器方式(yield)=======")
print("=======實現enumerate=======")

def get_tuple(obj):
    num = -1
    for item in obj:
        num += 1
        yield num, item

for item in get_tuple(list02):
    print(item)