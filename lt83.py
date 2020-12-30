# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        low = head
        fast = head.next
        while low and fast:
            if low.val == fast.val:
                low.next = fast.next
                fast = fast.next
            else:
                low = fast
                fast=fast.next
        return head