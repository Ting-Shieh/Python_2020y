
# class MyRangeIterator:
#     def __init__(self, stop):
#         self.__start = -1
#         self.__stop = stop
#
#     def __next__(self):
#         if self.__stop -1 == self.__start:
#             raise StopIteration
#         self.__start += 1
#         return self.__start
#
# class MyRange:
#     def __init__(self, stop_value):
#         self.__stop_value = stop_value
#
#     def __iter__(self):
#         return MyRangeIterator(self.__stop_value)
#
#
# """
# for item in MyRange(5):
#     print(item)
# """
# # 循環1次 計算1次  返回一次
# for item in MyRange(8):
#     print(item)


class MyRange:
    def __init__(self, stop_value):
        self.__stop_value = stop_value

    def __iter__(self):
        number = -1
        while number < self.__stop_value-1:
            number += 1
            yield number



# 循環1次 計算1次  返回一次
for item in MyRange(8):
    print(item)


def my_range(stop):
    number = -1
    while number < stop - 1:
        number += 1
        yield number

for item in my_range(5):
    print(item)