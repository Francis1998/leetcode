# Definition for a binary tree node.
import sys
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
#         def build(nums:List[int],lo int,hi int) -> TreeNode:
#             if lo>hi:
#                 return null
#             index = -1
#             maxVal= sys.maxsize
#             for i in range(lo,hi+1):
#                 if maxVal < nums[i]:
#                     index = i
#                     maxVal = nums[i]
#             root = TreeNode(maxVal)
#             root.left = build(nums,lo,index-1)
#             root.right = build(nums,index+1,hi)
#             return root
#         return build(nums,len(nums)-1)
lo = 10
hi = 100
for i in range(lo,hi+1):
    print(i)