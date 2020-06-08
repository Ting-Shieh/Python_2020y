game_map=[
    [2, 0, 2, 0],
    [2, 4, 2, 2],
    [2, 4, 0, 4],
    [0, 0, 2, 2]
]

# TODO
# 將列表中的0 放到列表尾巴
# [0, 4, 0, 0] -> [4, 0, 0, 0]


# # 取出列表中的非0數字，放到新列表
# # 在判斷原列表中有多少0，添加到新列表
# def zeno_to_end(list_target):
#     # 法1
#     # new_list = []
#     # for item in list_target:
#     #     if item != 0:
#     #         # [0, 4, 0, 0] -> [4]
#     #         new_list.append(item)
#     #         # 在判斷原列表有多少0，添加到新列表
#     #         for i in range(list_target.count(0)):
#     #             new_list.append(0)
#     # return new_list
#
#     # 法2
#     # 列表推倒式
#     new_list = [item for item in list_target if item != 0]
#     # 重複生成1個[0] 和 新列表拼接
#     # [0] 的個數是目標列表中0的個數
#     new_list += [0]*list_target.count(0)
#     return new_list

# ----------------------------------------------------
# ----------------------------------------------------

# TODO 將列表中的0 放到列表尾巴
def zeno_to_end():
    # # TODO 因為列表特點，由前往後刪除，會倒指索引值變化，不太合適
    # # 先刪除0元素，在列表後追加
    # for item in list_target:
    #     if item == 0:
    #         list_target.remove(item)
    #         list_target.append(0)
    # # 返回列表
    # return list_target

    # TODO 由後向前 如果發現0 做刪除 再追加0
    # 索引 由後向前
    for i in range(len(list_target)-1, -1, -1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)

# print(zeno_to_end([2, 0, 2, 0]))


# TODO 合併相鄰相同元素
def merge():
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

    zeno_to_end()
    #        0,1,2,3 = (4 個)  -1  =>0,1,2(3個)
    for i in range(len(list_target)-1):
        if list_target[i] == list_target[i+1]:
            # 合併降後面的元素累加到前面元素上
            list_target[i] += list_target[i+1]
            # 刪除後面元素
            del list_target[i+1]
            # 再補0
            list_target.append(0)

# list_test = [2, 2, 2, 2]
# merge(list_test)
# print(list_test)


# TODO [左移]合併相鄰相同元素
# 將二為列表中的每一個列表取出，交給 merge() 操作
# [右移] 原始列表 先反轉  合併  反轉
def move_left():
    for line in game_map:
        # list_target 非固定
        # 因為在函數內部是局部作用域
        # 設定 全局變量(list_target)
        global list_target
        list_target = line
        merge()

# move_left()
# print(game_map)

# TODO [右移]合併相鄰相同元素
# 原始列表   ->  先反轉   ->  合併     -> 再反轉
# line   ->  list_target   ->  list_target     -> line
# [4,4,2,2] -> [2,2,4,4] -> [4,8,0,0] -> [0,0,4,8]
def move_right():
    for line in game_map:
        # list_target 非固定
        # 因為在函數內部是局部作用域
        # 設定 全局變量(list_target)
        global list_target
        # 反向賦值
        list_target = line[::-1]
        # 合併
        merge()
        # 再反轉
        line[::-1] = list_target
        # line = list_target[::-1] # 會造成 內存不同

# move_right()
# print(game_map)

# TODO
def square_matrix(game_map):
    for c in range(1, len(game_map)):  # 1 2 3
        for r in range(c, 4):
            # 值交換
            game_map[r][c - 1], game_map[c - 1][r] = game_map[c - 1][r], game_map[r][c - 1]


# TODO [上移]合併相鄰相同元素
def move_up():
    square_matrix(game_map)
    move_left()
    square_matrix(game_map)




# TODO [下移]合併相鄰相同元素
def move_down():
    square_matrix(game_map)
    move_right()
    square_matrix(game_map)


move_up()

print(game_map)

move_down()
print(game_map)