import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        dp_i10 = 0
        dp_i11 = -sys.maxsize
        dp_i20 = 0
        dp_i21 = -sys.maxsize
        for i in range(n):
            dp_i20 = max(dp_i20,dp_i21+prices[i])#sell
            dp_i21 = max(dp_i21,dp_i10-prices[i])#买
            dp_i10 = max(dp_i10,dp_i11+prices[i])
            dp_i11 = max(dp_i11, -prices[i])
        return dp_i20