"""
二叉樹  實現
1. 鏈式存儲 => Node 表示一個節點(值，左鏈接，右鏈接)
2. 分析遍歷過程
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Bitree:
    # 傳入樹根
    def __init__(self, root):
        self.root = root

    def preOrder(self, node):
        """
            先序遍歷(根左右)
        :return:
        """
        if node is None:
            return
        print(node.val, end="")
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        """
            中序遍歷(左根右)
        :return:
        """
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val, end="")
        self.inOrder(node.right)

    def postOrder(self, node):
        """
            後序遍歷(左右根)
        :return:
        """
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val, end="")

    def levelOrder(self,node):
        """
            層次遍歷
        :param node:
        :return:
        """




if __name__ == '__main__':
    b = Node("B")
    c = Node("C")
    a = Node("A",b,c)

    bt = Bitree(a)
    bt.preOrder(bt.root)
    print("\n")
    bt.inOrder(bt.root)
    print("\n")
    bt.postOrder(bt.root)