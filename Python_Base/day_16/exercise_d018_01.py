from common.list_helper import ListHelper
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

print("id = 102 =>", ListHelper.find_single(list01, condition03))
print("name = B =>", ListHelper.find_single(list01, condition04))

