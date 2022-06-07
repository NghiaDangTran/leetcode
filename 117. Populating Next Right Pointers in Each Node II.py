"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # curr=root?
        head=root
        temp=Node(-999)
        while head:
            curr=head
            temp2=temp
            while curr:
                if curr.left:
                    temp2.next=curr.left
                    temp2=temp2.next
                if curr.right:
                    temp2.next=curr.right
                    temp2=temp2.next
                curr=curr.next
            head=temp.next
            temp.next=None
        return root
        