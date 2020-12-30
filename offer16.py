# 实现函数double Power(double base, int exponent)，
# 求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n <0:
            return 1/self.myPow(x,-n)
        if n&1:
            return x*self.myPow(x,n-1)
        return self.myPow(x*x,n//2)
dp = Solution()
print(dp.myPow(2,3))