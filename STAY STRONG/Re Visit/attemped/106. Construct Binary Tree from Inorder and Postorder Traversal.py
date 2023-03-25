
[0,1,3,9,19,20,21]
[0,3,1,19,21,20,9]
[1,2,3,5,6,7,8,9,18,20,21]
[1,3,2,6,8,7,5,18,21,20,9]
start with post[-1]
find idx of that 

rec (inorder,curr):
    if anythign return:
    
    new tree=tree(curr)


    tree.left=rec(in[0:curr],in[(0+curr)//2])
    tree.right=rec(in[curr+1:],in[(curr+1)//2])


class Solution:
    def buildTree(self, ino: List[int], post: List[int]) -> Optional[TreeNode]:
        if not post or not ino: return None 
        
        tree=TreeNode(post.pop())
        idx=ino.index(tree.val)
        tree.right=self.buildTree(ino[idx+1:],post)

        tree.left=self.buildTree(ino[:idx],post)
        return tree