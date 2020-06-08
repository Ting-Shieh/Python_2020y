class Employee:
    def __init__(self, base_salary=0):
        self.base_salary = base_salary
    def calc_salary(self):
        raise NotImplementedError()

    def __str__(self):
        return "底薪:%d。" % (self.base_salary)

    def __repr__(self):
        return "Employee(%d)" % self.base_salary

class IT(Employee):
    def __init__(self, base_salary=0, profit=0):
        super().__init__(base_salary)
        self.profit = profit


    def calc_salary(self):
        return self.base_salary + self.profit


class Seller(Employee):
    def __init__(self, base_salary=0, sell=0):
        super().__init__(base_salary)
        self.sell = sell

    def calc_salary(self):
        return self.base_salary + self.sell * 0.05


class EmpManager:
    def __init__(self):
        self.__emp_list = []


    @property
    def emp_list(self):
        return self.__emp_list

    def add_emp(self, emp):
        if not isinstance(emp, Employee):
            print("非繼承Employee")
        else:
            self.__emp_list.append(emp)

    def calc_totol_salary(self):
        totol_salary = 0
        for item in self.__emp_list:
            totol_salary += item.calc_salary()
        return totol_salary


manager = EmpManager()
manager.add_emp(IT(38000,2000))
manager.add_emp(Seller(25000,12000))
res = manager.calc_totol_salary()
print(res)

Employee01 = Employee(45000)
print(Employee01)