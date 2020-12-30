# Definition for singly-linked list. O(n) 时间复杂度和 O(1) 空间复杂度
# class ListNode:   快慢到一半，慢的不断反转链表
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast=fast.next.next
            slow.next,slow,prev = prev,slow.next,slow
        if fast:
            slow = slow.next
        while slow and slow.val == prev.val:
            slow=slow.next
            prev=prev.next
        return prev==None
