import math
class Solution:
    def getPermutation(self, n, k):
        num = [str(i) for i in range(1, n+1)]
        res = ""
        n -= 1
        while n > -1:
            t = math.factorial(n) #数量
            loc = math.ceil(k / t)  -1
            res += num[loc]
            num.pop(loc)
            k %= t
            n -= 1
        return res

print( )