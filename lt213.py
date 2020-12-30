# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，
# 这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，
# 系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。
# 示例 1：
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*105
        if len(nums)==0:
            return 0
        if len(nums)<=3:
            return max(nums)
        dp[0]=nums[0]
        dp[1]=max(dp[0],nums[1])
        for n in range(2,len(nums)-1):
            dp[n]=max(dp[n-1],dp[n-2]+nums[n])
        m1 = dp[len(nums)-2]

        nums = nums[1:]
        dp1 = [0]*105
        dp1[0]=nums[0]
        dp1[1]=max(dp1[0],nums[1])
        for n in range(2,len(nums)):
            dp1[n]=max(dp1[n-1],dp1[n-2]+nums[n])
        m2 = dp1[len(nums)-1]
        return max(m1,m2)