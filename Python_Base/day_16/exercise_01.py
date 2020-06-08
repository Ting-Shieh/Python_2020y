import time


# TODO 根據年月日計算是星期幾
def get_week(year, month, day):
    time_tuple = time.strptime('%d/%d/%d' % (year, month, day), '%Y/%m/%d')
    week_tuple = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")

    return week_tuple[time_tuple[6]]


# TODO 依據生日，計算活了多少天
def life_days(birthday):
    time_tuple = time.strptime(birthday, '%Y/%m/%d')
    # 時間元祖轉乘時間搓
    birth_second = time.mktime(time_tuple)
    # 生活總秒數 = 當前時間戳-出生時時間戳
    life_second = time.time()- birth_second
    return life_second/60/60//24


if __name__ == '__main__':
    print("-------根據年月日計算是星期幾---------")
    print(get_week(2020,4,29))
    print("-------依據生日，計算活了多少天---------")
    print(life_days('1991/04/29'))