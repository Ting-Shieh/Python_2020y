"""
迭代圖形管理器
"""
class Graphic:
    """
    作為迭代類要有
    __next__ 標誌
    """
    def __init__(self, data):
        self.__targets = data
        self.__index = -1

    def __next__(self):
        if self.__index >= len(self.__targets) -1:
            raise StopIteration
        self.__index +=1
        return self.__targets[self.__index]


"""
作為容器的類別
要有 __iter__  標誌
"""
class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, obj):
        self.__graphics.append(obj)

    def __iter__(self):
        return Graphic(self.__graphics)



manager = GraphicManager()
manager.add_graphic("T")
manager.add_graphic("F")
manager.add_graphic("R")

for item in manager:
    print(item)