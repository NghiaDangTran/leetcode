# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        mid=len(nums)//2        
        

        if nums==[]:
                return None

        return TreeNode(nums[mid],self.sortedArrayToBST(nums[0:mid]),self.sortedArrayToBST(nums[mid+1:]))

#  trick to solve is dont care about the order of the tree the only thing we need is the height of the tree , ingeneral this can make a tree from list