# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
# 每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
class Solution:
    def cuttingRope(self, n: int) -> int:
        memo = [i for i in range(n+1)]
        for i in range(4,n+1):
            for j in range(1,i//2+1):
                if memo[j]*memo[i-j]>memo[i]:
                    memo[i]=memo[j]*memo[i-j]
        if n<=3:
            return int(memo[n]-1)
        else:
            return memo[n]%1000000007