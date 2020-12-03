class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None
class Solution:
    def findMaximumXOR(self,nums):
        root = TrieNode()
        for num in nums:
            cur = root
            for i in range(32,-1,-1):
                tmp = num&1<<i
                if tmp:
                    if not cur.one:
                        cur.one = TrieNode()
                    cur = cur.one
                else:
                    if not cur.zero:
                        cur.zero = TrieNode()
                    cur = cur.zero
        res = 0
        for num in nums:
            cur = root
            val = 0
            for i in range(32,-1,-1):
                tmp = num & 1<<i
                if cur.zero and cur.one:
                    if tmp:
                        cur = cur.zero
                    else:
                        cur = cur.one
                    val += 1 << i
                else:
                    if (cur.zero and tmp) or (cur.one and not tmp):
                        val += 1 << i
                    cur = cur.one or cur.zero
            res = max(res,val)
        return res        