# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

        
    def isBalanced(self,root):
        if root:
            print(abs(self.Pdepth(root.left,0,1) - self.Pdepth(root.right,0,1)))
            if abs(self.Pdepth(root.left,0,1) - self.Pdepth(root.right,0,1))>1:
                
                return False
           

            return  self.isBalanced(root.left) and  self.isBalanced(root.right)

           

        return True
        
      
    
    
    def Pdepth(self,root,maxlv,lv):
        if root:
            
            if lv > maxlv:
                maxlv = lv
            maxlv=self.Pdepth(root.left,maxlv,lv+1)
            maxlv=self.Pdepth(root.right,maxlv,lv+1)
        
        
        return maxlv

#  new trick check similar question