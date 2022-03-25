# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def setNex(self, a):
        self.next=a

obj=ListNode(4)
obj.setNex(ListNode(5))
# class Solution:
#     def getIntersectionNode(self, headA, headB):
#         h = set()
#         while headA:
#             h.add(headA)
#             headA = headA.next
        
#         while headB:
#             if headB in h:
#                 return headB
#             headB = headB.next



#         p1 = headA
#         p2 = headB
#         while p1 != p2:
#             if p1:
#                 p1 = p1.next
#             else:
#                 p1 = headB
#             if p2:
#                 p2 = p2.next
#             else:
#                 p2 = headA
            
#         return p1

 trick fast and slow pointer in linked list is that loop again to the orther node in the orhter list
 and trick with set it not only not remove same value but also sort it based on the hash value


# {ListNode{val: 4, next: ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}}

# {ListNode{val: 4, next: ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}, ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}

# {ListNode{val: 4, next: ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}, ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}, ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}

# {ListNode{val: 4, next: ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}, ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}, ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}, ListNode{val: 4, next: ListNode{val: 5, next: None}}}

# {ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}, ListNode{val: 4, next: ListNode{val: 5, next: None}}, ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}, ListNode{val: 4, next: ListNode{val: 1, next: ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}, ListNode{val: 5, next: None}}


