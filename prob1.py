
# def twoSum( nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     result=[]
#     for i in range(len(nums)):
#         find=target-nums[i]
#         for j in range(len(nums)):
#             if(j!=i and find==nums[j]):
#                 result.append(nums[j])
#     print(result)




# twoSum( [2,7,11,15],9)


# *2)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        