"""
题目：设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈（避免审核不通过我就不放完整题目了）
思路：用python写，栈用数组实现，一开始是想用一个变量来存最小值，但是那样一旦栈发生了变化，那每次都要查找了，
所以再用一个数组（栈）把历史最小元素都存了起来，保持最小的在栈顶（数组最后一个）。
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = []#用来保存所有历史最小元素，保持栈顶（数组最后一个）是最小元素
        

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.min) == 0 or self.min[-1] >= x:#
            self.min.append(x)
        

    def pop(self) -> None:
        if len(self.data) != 0:
            if self.data[-1] == self.min[-1]:#出栈的是最小值，就都要出
                del(self.data[-1])
                del(self.min[-1])
            else:
                del(self.data[-1])
        

    def top(self) -> int:
        if len(self.data) != 0:
            return self.data[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.min) != 0:
            return self.min[-1]
        else:
            return None
