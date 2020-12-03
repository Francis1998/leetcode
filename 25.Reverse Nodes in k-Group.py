# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reversePart(self,head,tail):
        prev = tail.next
        p = head
        while prev!=tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail,head
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        hair = ListNode(0)
        hair.next = head
        pre = hair
        
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            tailnext = tail.next
            head,tail = self.reversePart(head,tail)
            pre.next = head
            tail.next = tailnext
            pre = tail
            head = tail.next
        return hair.next
        