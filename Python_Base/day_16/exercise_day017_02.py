"""
員工管理器
"""

class Employee:
    def __init__(self, data):
        self.__emp = data
        self.__index = -1

    def __next__(self):
        if self.__index >= len(self.__emp)-1:
            raise StopIteration
        self.__index += 1
        return self.__emp[self.__index]


class EmployeeManager:
    def __init__(self):
        self.__Employees = []

    def add_emp(self, obj):
        self.__Employees.append(obj)

    def __iter__(self):
        return Employee(self.__Employees)


manager = EmployeeManager()
manager.add_graphic("A01")
manager.add_graphic("B02")
manager.add_graphic("C03")

for item in manager:
    print(item)