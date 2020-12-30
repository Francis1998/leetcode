# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的
# ，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def sum(l1):
            sum = 0
            base = 1
            while l1:
                sum +=l1.val*base
                base*=10
                l1=l1.next
            return sum
        res = sum(l1)+sum(l2)
        tail = ListNode()
        if res ==0:
            return tail
        p = tail
        while res:
            tail.next = ListNode(val=res%10)
            res//=10
            tail = tail.next
        return p.next

