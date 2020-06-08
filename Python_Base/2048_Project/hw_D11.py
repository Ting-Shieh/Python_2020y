class Skill:
    def __init__(self, name="", atk_ratio=0.1, duration=0.1, cost_mp=0):
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration
        self.cost_mp = cost_mp

    @property
    def atk_ratio(self):
        return self.__atk_ratio
    @atk_ratio.setter
    def atk_ratio(self, val):
        if 0.1 <= val <=5:
            self.__atk_ratio = val
        else:
            raise ValueError('攻擊比例不再區間內')


    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, val):
        if 0.1 <= val <= 10:
            self.__duration = val
        else:
            raise ValueError('持續時間不再區間內')

    @property
    def cost_mp(self):
        return self.__cost_mp

    @cost_mp.setter
    def cost_mp(self, val):
        if 0 <= val <= 100:
            self.__cost_mp = val
        else:
            raise ValueError('攻擊比例不再區間內')


skill_list = [
    Skill("降龍18掌", 3, 2, 50),
    Skill("9陰白骨爪", 2, 4, 30),
    Skill("萬佛歸宗", 0.5, 8, 0),
    Skill("千手觀音", 0.1, 9, 3)
]

def find01():
    for item in skill_list:
        if item.name == '降龍18掌':
            return item
        else:
            raise ValueError('無此存在')

s01 = find01()
if s01:
    print(s01.name)


def find02():
    s_list = []
    for item in skill_list:
        if item.cost_mp == 0:
            s_list.append(item)
    return s_list

res = find02()

for item in res:
    print(item.name)

def find03():
    # result ={}
    # for item in skill_list:
    #     result.setdefault(item.name, item.duration)
    return { item.name: item.duration for item in skill_list }

res = find03()
for k,v in res.items():
    print(k,v)


def delete():
    count = 0
    for i in range(len(skill_list)-1, -1, -1):
        if skill_list[i].cost_mp == 0:
            del skill_list[i]
            count += 1
    return count

# res = delete()
# # print(res)


def find_big_atk():
    # big_val = 0
    # res = {}
    # for item in skill_list:
    #     if item.atk_ratio > big_val:
    #         big_val = item.atk_ratio
    #         res[item.name] = big_val
    # return res
    big_val = skill_list[0]
    for i in range(1,len(skill_list)):
        if big_val.atk_ratio < skill_list[i].atk_ratio:
            big_val = skill_list[i]

    return big_val
res = find_big_atk()
print(res.name)

def asc_sort():
    # 最後一個用索引加1的方式
    # 外層控制次數
    for r in range(len(skill_list)-1):
        for c in range(r+1, len(skill_list)):  # 當前元素後一個往下比較
            if skill_list[r].duration > skill_list[c].duration:
                # 換位子
                # 換對象還是換數據(.xxx) 
                skill_list[r], skill_list[c] = skill_list[c], skill_list[r]

    # 不用return 因為直接對列表的值做操作

asc_sort()
for item in skill_list:
    print(item.name)


import sys
print(sys.argv)