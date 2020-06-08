class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    def __str__(self):
        return "%s--%d--%d" %(self.name, self.atk, self.hp)

    def __repr__(self):
        return "Enemy('%s', %d, %d)" % (self.name, self.atk, self.hp)


e01 = Enemy("test1", 100, 50)
print(e01)
# 克隆 => 修改新對象，不改變原對象
e02 = eval(repr(e01))
e02.name = "test2"
print(e02)
print(e01)