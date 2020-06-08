


class Player:
    def __init__(self, atk=10, hp=100):
        self.atk = atk
        self.hp = hp

    # 傳入一個物件當參數
    def attack(self, enemy):
        print("玩家攻擊")
        enemy.damage(self.atk)

    def damage(self,val):
        print("i hurt")
        self.hp -= val
        if self.hp <=0:
            print("Game Over")
class Enemy:
    def __init__(self, hp=100, atk=99):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        print("get hurt")
        self.hp -= value

        if self.hp <= 0:
            print("敵人掛掉了喔~~")

    def attack(self, player):
        print("player gets hurt")
        player.damage(self.atk)
