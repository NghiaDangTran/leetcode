# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
[1,2,4,5,3,6,7]
[4,5,2,6,7,3,1]
1: [4,5,2,6,7,3] node 1
idx=4
1.right=construc([3,6,7],[ [4,5,2,6,7,3]])
1.right.3 idx=2 
1.right.right=construc([7],[ [4,5,2,6,7]])
1.3.7 
1,right, left=construc([3,6,7],[ [4,5,2,6]])

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        if not pre: return 
        if len(pre)==1:
            return TreeNode(post.pop())

        curr = TreeNode(post.pop())
        idx=pre.index(post[-1])
        curr.right=self.constructFromPrePost(pre[idx:],post)
        curr.left=self.constructFromPrePost(pre[1:idx],post)
        return curr


HOme work do from post to pre:

6T(n/2)+1

         
            
            