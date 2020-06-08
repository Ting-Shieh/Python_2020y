
class QueueError(Exception):
    pass


class SQueue:
    def __init__(self):
        self._elems = []

    # 判斷隊列是否為空
    def is_empty(self):
        return self._elems == []

    # 入隊
    def enqueue(self, val):
        return self._elems.append(val)


    # 出隊
    def dequeue(self):
        if not self._elems:   # 空列表
            raise QueueError("Queue is empty")
        return self._elems.pop(0)  # 彈出第一個數據


    # 反轉出隊
    def redequeue(self):
        if not self._elems:   # 空列表
            raise QueueError("Queue is empty")
        for i in range(len(self._elems)-1,-1,-1):
            return self._elems.pop(i)  # 彈出第一個數據



if __name__ == '__main__':
    sq = SQueue()
    for i in range(15):
        sq.enqueue(i)
    while not sq.is_empty():
        print(sq.redequeue())