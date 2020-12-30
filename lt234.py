# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 请判断一个链表是否为回文链表。
# 示例 1:
# 输入: 1->2
# 输出: false
# 示例 2:
# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        p = head
        if p==None:
            return True
        while p:
            res.append(p)
            p=p.next
        lens = len(res)
        if lens %2 == 0:
            mid = lens//2
            if res[:mid] == res[lens-1:mid-1:-1]:
                return True
        else:
            mid = lens//2
            if res[:mid] == res[lens-1:mid:-1]:
                return True
        return False