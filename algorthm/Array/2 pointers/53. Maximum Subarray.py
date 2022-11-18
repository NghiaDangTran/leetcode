# 2 pointer approach
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        curr2=0
        for i in nums:
            curr=max(0,curr+i)
            curr2=max(curr,curr2)
            
        if curr2==0:
            return sorted(nums)[-1]
        
       
            
        return curr2
        
# divide and conquare aproapre
