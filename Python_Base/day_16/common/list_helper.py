"""
定義項目中所有對容器的操作
"""
"""
def condition01(item):
    return item.durationd >10

def condition(item):
    return 102<=item.id<=105

def find(func):
    for item in list01:
        if func(item):
            yield item
"""

"""
如果想再類裡面放方法，就用@staticmethod
"""

class ListHelper:
    """
    列表助手列
    """
    @staticmethod
    def find_all(iterable_target, func_condition):
        """
        在可迭代對象中，查找滿足任意條件的所有元素。
        :param iterable_target: 可迭代對象(數據)
        :param func_condition: 搜索條件(邏輯)
        :return: 生成器對象
        """
        for item in iterable_target:
            if func_condition(item):
                yield item


    @staticmethod
    def find_single(iterable_target, func_condition):
        """
        在可迭代對象中，查找滿足任意條件的單一元素。
        :param iterable_target: 可迭代對象(數據)
        :param func_condition: 搜索條件(邏輯)
        :return: 對象
        """
        for item in iterable_target:
            # if item.name == "B":
            if func_condition(item):
                return item

    @staticmethod
    def for_skill(iterable_target, func_condition):
        """
        在可迭代對象中，查找滿足任意條件的單一元素。
        :param iterable_target: 可迭代對象(數據)
        :param func_condition: 搜索條件(邏輯)
        :return: 對象
        """
        sum_value = 0
        for item in iterable_target:
            sum_value += func_condition(item)
        return sum_value

    @staticmethod
    def select(iterable_target, func_condition):
        """
        在可迭代對象中，根據條件選擇屬性
        :param iterable_target: 可迭代對象(數據)
        :param func_condition: 搜索條件(邏輯)
        :return: 對象
        """
        for item in iterable_target:
            yield  func_condition(item)

    @staticmethod
    def get_max(iterable_target, func_condition):
        """
        在可迭代對象中，根據條件獲取最大變數
        :param iterable_target:
        :param func_condition:
        :return: 最大元素
        """
        max_value = iterable_target[0]
        for i in range(1, len(iterable_target)):
            # if max_value.atk < iterable_target[i].atk:
            if func_condition(max_value) < func_condition(iterable_target[i]):
                max_value = iterable_target[i]
        return max_value

    @staticmethod
    def get_sort(iterable_target, func_condition):
        """
            在可迭代對象中，根據條件升序排列
        :param iterable_target: 可迭代對象
        :param func_condition: 排序條件
        :return:
        """
        for i in range(len(iterable_target) - 1):
            for c in range(i + 1, len(iterable_target)):
                if func_condition(iterable_target[i]) > func_condition(iterable_target[c]):
                    iterable_target[i], iterable_target[c] = iterable_target[c], iterable_target[i]
        for item in iterable_target:
            yield item

    @staticmethod
    def get_max_len(iterable_target, func_condition):
        max_len = iterable_target[0]
        for i in range(1, len(iterable_target)):
            if func_condition(max_len) < func_condition(iterable_target[i]):
                max_len = iterable_target[i]
        return len(max_len)