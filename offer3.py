class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        l = len(nums)
        count = {}
        max_count = -1
        max_num = 0
        for i in range(l):
            count.setdefault(nums[i],0)
            count[nums[i]]+=1
            if max_count<count[nums[i]]:
                max_count = count[nums[i]]
                max_num = nums[i]
            if count[nums[i]] >= l>>1:
                return nums[i]
        return max_num