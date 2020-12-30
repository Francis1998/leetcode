class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x = str(x)
            s = x[-1:0:-1]
            res = -1*int(s)
            return res if -2**31<=res<=2**31-1 else 0
        x = str(x)
        s = x[::-1]
        res = int(s)
        return res if -2**31<=res<=2**31-1 else 0
