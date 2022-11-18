class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res,pre,suf=[1]*len(nums),1,1
        for i in range(len(nums)):
            res[i]*=pre
            pre*=nums[i]
            res[-1-i]*=suf
            suf*=nums[-1-i]
            
        return res
            
        Start pet coding session