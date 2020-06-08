
class AtkError(Exception):
    def __init__(self, id, message, code):
        self.id = id
        self.message = message
        self.code = code



class Enemy:
    def __init__(self, atk, name):
        self.atk = atk
        self.name = name

    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self, val):
        if 0 <= val <= 100:
            self.__atk = val
        else:
            raise AtkError(101, "攻擊力範圍超出設定", " 0 ~ 100")


if __name__ == '__main__':
    try:
        e01 = Enemy(150,"TT")
        print(e01.atk)
        print(e01.name)
    except AtkError as e:
        print("錯誤ID: ", e.id)
        print("錯誤message&code: %s & %s" %(e.message, e.code))