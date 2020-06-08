class Graphic:
    def calc_area(self):
        """
        如果子類 部重寫父類
        及拋出異常
        :return:
        """
        raise NotImplementedError()


class Circle(Graphic):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14*self.radius**2


class Rectangle(Graphic):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width*self.height


class GraphicManager:
    def __init__(self,):
        self.__list_graphic = []

    # 只讀功能
    @property
    def list_graphic(self):
        return self.__list_graphic

    def add_graphic(self, graphic):
        """
        添加物件
        :param graphic:
        :return:
        """
        if not isinstance(graphic, Graphic):
            raise ValueError("非繼承Graphic")
        else:
            self.__list_graphic.append(graphic)

    def calc_total_area(self):
        total_area = 0
        for item in self.__list_graphic:
            total_area += item.calc_area()
        return  total_area

c01 = Circle(5)
r01 = Rectangle(10, 20)
manager = GraphicManager()
manager.add_graphic(c01)
manager.add_graphic(r01)
res = manager.calc_total_area()
print(res)