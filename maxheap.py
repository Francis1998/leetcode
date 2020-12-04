class MaxHeap():
    #parent: (i-1)//2 left: 2i + 1 right: 2i + 2
    # pop需要 shift_down(0) add需要shift_up(count)
    def __init__(self,maxsize=None):
        self.maxSize = maxsize
        self.li = [None]*maxsize
        self.count = 0
    def add(self,value):
        
