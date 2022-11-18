class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref,surf,curr,curr2,savedata=1,1,nums[0],nums[-1],nums[0]
        for i in range(len(nums)):
            if nums[i]==0:
                savedata=max(curr,savedata)
                curr=0
                pref=1
            else:
                pref*=nums[i]
                curr=max(curr,pref)
        savedata=max(savedata,curr)
        sd2=nums[-1]
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                sd2=max(sd2,curr2)
                curr2=0
                surf=1
            else:
                surf*=nums[i]
                curr2=max(curr2,surf)
        sd2=max(sd2,curr2)
        return max(savedata,sd2)
            
        
            
            
        
        

    
            
        return 0
        