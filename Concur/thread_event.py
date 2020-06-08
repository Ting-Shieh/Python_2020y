"""
Event 應用範例
線程互斥演練
"""
from threading import Thread, Event

# e = Event()
# print("state: ", e.is_set())
# e.set()
# print("after set state: ", e.is_set())
# e.clear()
# print("after set is cleared state: ", e.is_set())

s = None
e = Event()
def Ying():
    """
    分支線程
    :return:
    """
    print("Ying 前來拜見")
    global s
    s = "天王蓋地虎"
    e.set()


# TODO 主線程

t = Thread(target=Ying)

t.start()

print("說對暗號就是自己人")

e.wait()  # 等待e 被set


if s == "天王蓋地虎":
    print("寶塔鎮河妖")
else:
    print("打死他!!")

t.join()