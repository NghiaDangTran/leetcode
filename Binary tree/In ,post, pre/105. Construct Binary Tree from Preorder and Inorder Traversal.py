# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, pre: List[int], ino: List[int]) -> Optional[TreeNode]:
        if not pre or not ino: return None
        
        tree=TreeNode(pre.pop(0))
        idx=ino.index(tree.val)
        
        tree.left=self.buildTree(pre,ino[0:idx])
        tree.right=self.buildTree(pre,ino[idx+1:])
        return tree