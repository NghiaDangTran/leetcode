# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
       
        return self.Pdepth(root,0,1)
        
        
    def Pdepth(self,root,maxlv,lv):
        if root:
            print(maxlv)
            if lv > maxlv:
                maxlv = lv
            maxlv=self.Pdepth(root.left,maxlv,lv+1)
            maxlv=self.Pdepth(root.right,maxlv,lv+1)
        
        
        return maxlv
            
            
            