# 转一个单链表。
# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
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
    def reverseList(self, head: ListNode) -> ListNode:
        tail = ListNode(0)
        p_tail = tail
        p = head
        res = []
        while p:
            res.append(p.val)
            p=p.next
        for i in range(len(res)):
            tail.next = ListNode(res.pop())
            tail=tail.next
        return p_tail.next