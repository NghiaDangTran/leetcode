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
        stack=[root]
        while stack:
            curr=stack.pop()
            if curr.right and curr.left:
                curr.left.next=curr.right
                if curr.next:
                    curr.right.next=curr.next.left
                stack.append(curr.left)
                stack.append(curr.right)
        