import sys
class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.seek = []
        self.seek.append(sys.maxsize)

    def push(self, x: int) -> None:
        self.data.append(x)
        top = self.seek[-1]
        self.seek.append(min(top,x))


    def pop(self) -> None:
        self.data.pop(-1)
        self.seek.pop(-1)

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.seek[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()