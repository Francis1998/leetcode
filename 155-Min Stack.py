class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.seek = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.seek)==0:
            self.seek.append(0)

    def pop(self) -> None:
        self.data.pop(-1)

    def top(self) -> int:
        return self.data[0]

    def getMin(self) -> int:
        return self.data[self.seek[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()