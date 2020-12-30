# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        hair = ListNode()
        res = hair
        while p1 and p2:
            if p1.val>=p2.val:
                hair.next = p2
                p2=p2.next
            else:
                hair.next = p1
                p1=p1.next
            hair=hair.next
        if p1:
            hair.next =p1
        else:
            hair.next = p2
        return res.next