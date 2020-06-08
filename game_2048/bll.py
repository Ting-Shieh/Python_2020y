"""
負責處理程序的業務邏輯
GameCoreController(靜態方法)
"""
import random
from model import Location


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
                [2, 0, 2, 0],
                [2, 4, 2, 2],
                [2, 4, 0, 4],
                [0, 0, 2, 2]
            ]
        self.__list_empty_location = []
    @property
    def map(self):
        return self.__map

    # TODO 將列表中的0 放到列表尾巴
    def __zero_to_end(self):
        """
        TODO 由後向前 如果發現0 做刪除 再追加0
        :return:
        """
        # 索引 由後向前
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)


    # TODO 合併相鄰相同元素
    # 思路
    # [0,2,0,2] -> [4,0,0,0]
    #  0 1 2 3
    #        x
    # [2,2,0,0] -> [4,0,0,0]
    # [4,2,0,0]
    # [4, 0, 0, 0]
    # [2,2,2,2] -> [4,4,0,0]
    # [2,0,4,0] -> [2,4,0,0]
    # 先將0元素移動到末尾
    # 再合併相鄰的元素
    # 如果相鄰的元素相同 合併
    # 補0
    def __merge(self):
        """
        合併相鄰相同元素
        :return:
        """
        self.__zero_to_end()
        #        0,1,2,3 = (4 個)  -1  =>0,1,2(3個)
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                # 合併降後面的元素累加到前面元素上
                self.__list_merge[i] += self.__list_merge[i + 1]
                # 刪除後面元素
                del self.__list_merge[i + 1]
                # 再補0
                self.__list_merge.append(0)



    # 將二為列表中的每一個列表取出，交給 merge() 操作
    # [右移] 原始列表 先反轉  合併  反轉
    def move_left(self):
        """
        [左移]合併相鄰相同元素
        :return:
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    # 原始列表   ->  先反轉   ->  合併     -> 再反轉
    # line   ->  list_target   ->  list_target     -> line
    # [4,4,2,2] -> [2,2,4,4] -> [4,8,0,0] -> [0,0,4,8]
    def move_right(self):
        """
         [右移]合併相鄰相同元素
        :return:
        """
        for line in self.__map:
            # 反向賦值
            self.__list_merge = line[::-1]
            # 合併
            self.__merge()
            # 再反轉
            line[::-1] = self.__list_merge

    def move_up(self):
        """
        [上移]合併相鄰相同元素
        :return:
        """
        self.__square_matrix()
        self.move_left()
        self.__square_matrix()

    def move_down(self):
        """
        [下移]合併相鄰相同元素
        :return:
        """
        self.__square_matrix()
        self.move_right()
        self.__square_matrix()

    # TODO
    def __square_matrix(self):
        for c in range(1, len(self.__map)):  # 1 2 3
            for r in range(c, len(self.__map)):
                # 值交換
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]


    def generate_new_number(self):
        """
        生成新數字
        :return:
        """
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return

        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r_index][loc.c_index] = self.__select_random_number()
        # 因為在該位置上生成了新數字，所以該位置就不會是空位置
        self.__list_empty_location.remove(loc)

    def __select_random_number(self):
        return 4 if random.randint(1, 10) == 1 else 2


    def __get_empty_location(self):
        """
        每次統計空位置，都先清空之前數據，避免影響本次數據
        :return:
        """
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(Location(r, c))

    def is_game_over(self):
        """
            遊戲是否結束
        :return: False表示沒有結束。True表示結束。
        """
        # 是否有空位置
        if len(self.__list_empty_location) >0:
            return False
        # 判斷水平方向有沒有相同的元素
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])-1): # 0 1 2
                if self.__map[r][c] == self.__map[r][c+1]:
                    return False

        # 判斷垂直方向有沒有相同的元素
        for c in range(4):
            for r in range(3):
                if self.__map[r][c] == self.__map[r+1][c]:
                    return False

        return True
# --------------------測試代碼---------------------

if __name__ == '__main__':
    controller = GameCoreController()
    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()

    print(controller.map)