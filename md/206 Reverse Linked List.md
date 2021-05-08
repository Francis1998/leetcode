旋转链表，记录当前节点和前一节点，利用python的多重赋值，右边均为额外记录的局部变量的特性。但是赋值顺序有要求，先prev，再cur.next，最后cur

prev,cur = None, head

while cur:

​	prev, cur.next, cur = cur, prev, cur.next 

return prev

