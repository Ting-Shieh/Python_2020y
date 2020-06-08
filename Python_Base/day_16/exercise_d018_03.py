from common.list_helper import ListHelper

tuple01 = ([1, 1], [2, 2, 2, 2], [3, 3])
# for item in ListHelper.get_max(tuple01, lambda x: len(x)):
#     print(item)
# print(ListHelper.get_max_len(tuple01, lambda x: len(x)))
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
# *自己寫的*
# print(len(ListHelper.get_max(tuple01, lambda x: len(x))))
print(max(tuple01, key=lambda x: len(x)))
# *自己寫的*
# for item in ListHelper.select(list01, lambda item: (item.name, item.atk, item.duration)):
#     print(item)
for item in map(lambda item: (item.name, item.atk, item.duration),list01):
    print(item)
# min()
print(min(list01, key = lambda item: item.atk))

for item in sorted(list01, key=lambda item: item.duration, reverse=True):
    print(item)
