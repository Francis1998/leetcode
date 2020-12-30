# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def trace(preorder,inorder):
            root = TreeNode(preorder[0])
            in_index = inorder.index(preorder[0])
            root.left = trace(preorder[1:in_index+1],inorder[:in_index])
            root.right = trace(preorder[in_index+1:],inorder[in_index+1:])
            return root
a = [1,2,3]
print(a[1:2])