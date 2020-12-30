import collections
class LRUCache:
    
    def __init__(self, capacity: int):
        self.size = capacity
        self.dic = collections.OrderedDict()
    def get(self, key: int) -> int:
        if key in self.dic.keys():
            value=self.dic.pop(key)
            self.dic[key]=value
            return self.dic[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.dic.keys():
            self.dic.pop(key)
            self.dic[key]=value
        elif self.size == len(dic):
            self.dic.popitem(last=False)
            self.dic[key]=value
        else:
            self.dic[key]=value