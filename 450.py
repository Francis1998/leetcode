# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left or not root.right:
                root = root.left if not root.right else root.right
            else:
                node = root.left
                while node.right:
                    node = node.right
                root.val = node.val
                root.left = self.deleteNode(root.left,node.val)
        return root
row = 3 #row
column = 2#column
path = [[0 for _ in range(column)] for _ in range(row)]
print(path)