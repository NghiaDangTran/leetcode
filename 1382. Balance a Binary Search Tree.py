# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        
        
        data=[]
        
        def rec1(node):
            
            if not node: return
            
            
            
            rec1(node.left)
            data.append(node.val)

            rec1(node.right)

        rec1(root)
      
        def array_to_bst(array_nums):
            if not array_nums:
                return None
            mid_num = len(array_nums)//2
            node = TreeNode(array_nums[mid_num])
            node.left = array_to_bst(array_nums[:mid_num])
            node.right = array_to_bst(array_nums[mid_num+1:])
            return node
        return array_to_bst(data)
        #       
