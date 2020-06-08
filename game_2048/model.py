"""
數據模型
負責描述項目中需要操作的數據
"""

class Location:
    """
    位置
    """
    def __init__(self,r, c):
        self.r_index = r
        self.c_index = c