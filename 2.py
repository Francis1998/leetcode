class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        答题思路：从后往前寻找第一个升序对(i,j)即nums[i]<nums[j] 再从后往前找第一个大于nums[i]的数即为大数，交换着两个元素即将大数换到前面，然后将大数后面的部分倒序
        """
        n = len(nums)
        if n<2: return nums
        i = n-1
        while i>0 and nums[i-1]>=nums[i]:#要是前者大于等于后者 则不是要调整的目标 继续前移  ！第一遍出错就是这儿没有等于
            i -= 1
        if i==0 : #此数为最大数（之前写的 i==0 and nums[i]==max(nums)，判断冗余，现删除）
            return nums.reverse()
        else:                          
            j = n-1
            while j>i-1 and nums[j]<=nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
            for k in range((n-i) // 2):
                nums[i+k], nums[n-1-k] = nums[n-1-k], nums[i+k]
        return nums
dp = Solution()
print(dp.nextPermutation([1,2,3,4,6,9,5]))
dic = {'1':0}
print(any(list((dic.values()))))