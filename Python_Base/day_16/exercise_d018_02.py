from common.list_helper import ListHelper
class Skill:
    def __init__(self, id, name=None, atk=None, duration = None):
        self.id= id
        self.name = name
        self.atk = atk
        self.duration = duration

    def __str__(self):
        return self.name
list01 = [
    Skill(101, "A", 8000, 20),
    Skill(102, "B", 7000, 15),
    Skill(103, "C", 9000, 10),
    Skill(104, "D", 500, 15),
    Skill(105, "E", 7500, 25)
]

# # TODO 基礎邏輯
# def find03():
#     for item in list01:
#         if item.id == 102:
#             return item
#
# def find03():
#     for item in list01:
#         if item.name == "B":
#             return item
#
# # TODO 提出邏輯(變化點)
#
# # 尋找邏輯
# def condition03(obj):
#     return obj.id == 102
# # 尋找邏輯
# def condition04(obj):
#     return obj.name == "B"
#
# # TODO 提出邏輯(共同點)
# def find(func):
#     for item in list01:
#         # if item.name == "B":
#         if func(item):
#             return item
# 尋找邏輯
def condition03(obj):
    return obj.id == 102
# 尋找邏輯
def condition04(obj):
    return obj.name == "B"

for item in ListHelper.find_all(list01, lambda obj:  obj.duration > 10 ):
    print(item)
print("id = 102 =>", ListHelper.find_single(list01, lambda obj: obj.id == 102 ))
print("name = B =>", ListHelper.find_single(list01, lambda obj: obj.name == "B"))

# 練習2
# def sum01():
#     sum_value = 0
#     for item in list01:
#         sum_value += item.atk
#     return sum_value
#
#
# def sum02():
#     sum_value = 0
#     for item in list01:
#         sum_value += item.duration
#     return sum_value
#
# # 尋找邏輯
# def condition05(obj):
#     return obj.atk
# # 尋找邏輯
# def condition06(obj):
#     return obj.duration
#
# def sum(func):
#     sum_value = 0
#     for item in list01:
#         sum_value += func(item)
#     return sum_value

print("Total atk =>", ListHelper.for_skill(list01, lambda obj: obj.atk ))
print("Total duration =>", ListHelper.for_skill(list01, lambda obj: obj.duration))

# 練習4

print("Total Max-atk duration=>", ListHelper.get_max(list01, lambda obj: obj.atk))
print("Total Max-duration =>", ListHelper.get_max(list01, lambda obj: obj.duration))
# 練習5
# By攻擊力 進行升序排列
# By持續時間 進行升序排列
print("By 攻擊力 進行升序排列=>")
for item in  ListHelper.get_sort(list01, lambda obj: obj.atk):
    print(item, end='\t')
print("\nBy 持續時間 進行升序排列=>")
for item in  ListHelper.get_sort(list01, lambda obj: obj.duration):
    print(item, end='\t')
