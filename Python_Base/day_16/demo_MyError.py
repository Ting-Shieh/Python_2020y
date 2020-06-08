class AgeError(Exception):
    def __init__(self, message, code, id):
        # 錯誤訊息
        self.message = message
        # 錯誤代碼
        self.code = code
        # 錯誤編號
        self.id = id


class Wife:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if 23 <= value <= 30:
            self.__age = value
        else:
            raise AgeError("我不要","23 <= value <= 30", 101)


try:
    w01 = Wife(85)
    print(w01.age)
except AgeError as e:
    # print(e.args)
    print(e.id)
    print(e.message,e.code)