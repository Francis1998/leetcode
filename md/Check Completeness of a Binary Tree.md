class Solution:

  def isCompleteTree(self, root: TreeNode) -> bool:

​    has_None = False

​    q = [root]

​    while q:

​      p=q.pop(0)#层次遍历

​      if not has_None and not p:

​        has_None=True #第一次出现None

​      if has_None and p:

​        return False

​      if p:

​        q.extend([p.left,p.right]) #list可以添加None，但None不存在.left

​    return True