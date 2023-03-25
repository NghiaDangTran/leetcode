class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr=0
        curr_max=0
        
        for i in range(len(nums)):
            curr= max(0,curr+nums[i])
            curr_max=max(curr_max,curr)
        if curr_max==0:
            curr=nums[0]
            for i in range(len(nums)):
                curr=  max(curr,nums[i])
            return curr
        return curr_max
            
        
    def max(a,b):
        if a>b: 
            return a
        return b