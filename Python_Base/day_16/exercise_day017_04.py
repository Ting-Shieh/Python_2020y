class SkillIterator:
    def __init__(self, data):
        """
        物件
        :param data:
        """
        self.__target = data
        self.__index = -1

    # def __next__(self):
    #     """
    #     下個迭代對象
    #     :return:
    #     """
    #     # 如果沒有數據則拋出異常
    #     if self.__index >= len(self.__target)-1:
    #         raise StopIteration
    #     # 返回數據
    #     self.__index += 1  # 0
    #     return self.__target[self.__index]

class GraphicManager:
    def __init__(self):
        self.__skills = []

    def add_graphic(self, obj):
        self.__skills.append(obj)

    def __iter__(self):
        for item in self.__skills:
            yield item

manager = GraphicManager()
manager.add_graphic("T")
manager.add_graphic("F")
manager.add_graphic("R")

for item in manager:
    print(item)