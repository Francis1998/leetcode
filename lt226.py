# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#     4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root ==None:
            return None
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root