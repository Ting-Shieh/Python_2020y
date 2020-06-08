class Skill:
    def __init__(self, id, name=None, atk=None, duration = None):
        self.id= id
        self.name = name
        self.atk = atk
        self.durationd = duration

    def __str__(self):
        return self.name


list01 = [
    Skill(101, "A", 8000, 20),
    Skill(102, "B", 7000, 15),
    Skill(103, "C", 9000, 10),
    Skill(104, "D", 500, 15),
    Skill(105, "E", 7500, 25)
]

# 通過生成器函數 實現
# yield:向外返回  多個結果
# 1.atk>8000
def find_atk(num):
    for item in list01:
        if item.atk >= num:
            yield item
print('=========1.atk>8000==========')
for item in find_atk(8000):
    print('1.atk>8000: ',item)

for item in ( item for item in list01 if item.atk >= 8000):
    print('1.atk>8000: ',item)

# 2.查找103
# return:向外返回  1個結果
def find_target(num):
    for item in list01:
        if item.id == num:
            return item

print('=========2.查找103==========')
res = find_target(103)
print('2練習查找: ', res)

# 3.獲取 所有技能的名稱
print('=========3.獲取所有技能的名稱==========')
def find_all_name():
    for item in list01:
        yield item.name
print('3.獲取所有技能的名稱: ')
for item in find_all_name():
    print(item,end='\t')
print('\n3.獲取所有技能的名稱: ')
for item in ( item.name for item in list01 ):
    print(item,end='\t')


# TODO
# 獲取持續時間大於10的所有技能
# 獲取編號在102~105之間的所有技能

"""
函數式編成思想
"""
def condition01(item):
    return item.durationd >10

def condition(item):
    return 102<=item.id<=105

def find(func):
    for item in list01:
        if func(item):
            yield item

# for item in find(condition01):
#     print(item)
print("\n-------------ListHelper----------")

from common.list_helper import ListHelper
for item in ListHelper.find_all(list01, condition01):
    print(item)