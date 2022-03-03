# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root:
            targetSum=targetSum-root.val
            if root.left==None and root.right==None and targetSum==0 :
                return True
        else: return False
   
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)