# 100. Same Tree.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.private_sametree(p,q)
        
    def private_sametree(self,l,r):
        
        

        if l and r and (l.val==r.val) :
            return self.private_sametree(l.left,r.left)  and self.private_sametree(l.right,r.right)
        if  (not l and not r): return True
        else: return False



# Runtime: 23 ms, faster than 59.37% of Python online submissions for Same Tree.
# Memory Usage: 13.8 MB, less than 13.10% of Python online submissions for Same Tree.
# Next challenges:

# trick to solve this problem: 
# the first of all   l and r and (l.val==r.val)  will al ways garuntee that the left and right subtree are the same after that 
# recuresive call back to the function again to loop untill we get the end point.
# then we only need to check if the end point is the same becase if the left value is not the same it will handel by the else
# mean it false right away if the end point is not the same