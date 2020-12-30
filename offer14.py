# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1）2 2
# ，每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n==3:
            return 2
        dp=[0]*60
        dp[1]=1
        dp[2]=2
        dp[3]=3
        def trace(n1):
            max1 = 1
            for i in range(1,n1):
                if max1<dp[n1-i]*dp[i]:
                    max1 = dp[n1-i]*dp[i]
            return max1
        for i in range(4,n+1):
            dp[i]=trace(i)
        print(dp)
        return dp[n]
dp = Solution()
print(dp.cuttingRope(10))