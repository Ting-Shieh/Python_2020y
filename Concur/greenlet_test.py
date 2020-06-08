from greenlet import greenlet


def fun1():
    print("執行1")
    gr2.switch()
    print("結束fun1")

def fun2():
    print("執行2")
    gr1.switch()
    print("結束fun2")

# 將函數變成協成函數
gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()
