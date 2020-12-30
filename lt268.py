# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
# 进阶：
# 你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
# 示例 1：
# 输入：nums = [3,0,1]
# 输出：2
# 解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic = {}
        max = 0
        for i in nums:
            dic[i] = 1
        for i in range(0,len(nums)+1):
            if i not in dic:
                return i