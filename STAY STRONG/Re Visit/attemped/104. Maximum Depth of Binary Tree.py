# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        table=[]
        def rec(root,curr):
            
            if not root:
                return 0
            # if curr%2!=0:
            #     return root.val
            # if not root.left and not root.right:
            #     return curr

            # if len(table)==curr:
            #     table.append(root.val)
            # else:
            #     table[curr]+=root.val
            a=rec(root.left,curr+1)
            b=rec(root.right,curr+1)
        
            return 1+max(a,b)

        
        return rec(root,1)