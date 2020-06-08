class SkillIterator:
    def __init__(self, data):
        """
        物件
        :param data:
        """
        self.__target = data
        self.__index = -1

    def __next__(self):
        """
        下個迭代對象
        :return:
        """
        # 如果沒有數據則拋出異常
        if self.__index >= len(self.__target)-1:
            raise StopIteration
        # 返回數據
        self.__index += 1  # 0
        return self.__target[self.__index]

class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, obj):
        self.__skills.append(obj)

    def __iter__(self):
        """
        變成容器
        :return:
        """
        return SkillIterator(self.__skills)


manager = SkillManager()
manager.add_skill("001")
manager.add_skill("002")
manager.add_skill("003")

# # manager 必須是 可迭代對象
# # 自建一個可迭代對象
# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break


# 正常方法
for item in manager:
    print(item)
