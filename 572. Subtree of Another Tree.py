# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def CompareSub(root1, subroot1):
            if not root1 and not subroot1:
                return True
            if root1 and subroot1:
                return root1.val == subroot1.val and CompareSub(root1.right, subroot1.right) and CompareSub(root1.left, subroot1.left)

            return False

        def find(s, t):
            if s is None: return False
            if CompareSub(s, t): return True
            return find(s.left, t) or find(s.right, t)
        
        return find(root,subRoot)
       
        # return False
