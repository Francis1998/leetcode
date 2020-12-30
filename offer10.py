class Solution:
    def numWays(self, n: int) -> int:
        if n in [0,1]:
            return 1
        dp = [0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[n] = (dp[n-1]+dp[n-2])%1000000007
            print(dp[i],i)
        return dp[n]
dp = Solution()
print(dp.numWays(4))