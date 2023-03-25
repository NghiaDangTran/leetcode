class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr=sum(nums[0:k])
        res=curr
        for i in range(k,len(nums)):
            curr+=nums[i]
            curr-=nums[i-k]
            if curr>res:
                res=curr
        return res/k
        