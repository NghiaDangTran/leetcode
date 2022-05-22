class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        #  one of the trick here is that the key
        # word contiguous subarray whcih mean the 
        # you cant skip the elment between them then
        # sliding windows will work the best
        # currLengh=0
        # if target<=1: return 0
        # currsum=0
        # l=0
        # res=9999
        # for r in range(len(nums)):
        #     currsum+=nums[r]
        #     currLengh+=1
        #     if currsum>=target:
        #         res=min(currLengh,res)


            

        #     while currsum>=target:
                
        #         currsum-=nums[l]
        #         l+=1
        #         currLengh-=1
        #         if currsum>=target:
        #             res=min(currLengh,res)
        #         # print(currLengh,currsum)

                
            
        # if res==9999:
        #     return 0
        # return res
        currsum=0
        l=0
        res=9999
        for r in range(len(nums)):
            currsum+=nums[r]

            while currsum>=target:
                res=min(r-l+1,res)
                currsum-=nums[l]
                l+=1
        if res==9999:
            return 0
        return res
        #  this work but slow compare to orther