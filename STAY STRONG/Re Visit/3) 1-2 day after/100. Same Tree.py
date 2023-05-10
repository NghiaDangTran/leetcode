# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def rec(left,right):
            if (not left or not right) and left.val!=right.val:
                return False
            if not left and not right:                return True
            return rec(left.left,right.left) and rec(left.right,right.right)



