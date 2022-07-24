# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, arr) :
        
        if not arr:
            return 
        at=arr.index(max(arr))
        curr= TreeNode(arr[at])
        curr.left=self.constructMaximumBinaryTree(arr[:at])
        curr.right=self.constructMaximumBinaryTree(arr[at+1:])


        
        

        return curr
        
        
        
        