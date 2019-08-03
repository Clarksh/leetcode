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