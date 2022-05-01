class Solution:
    def findPeakElement(self, nums) -> int:
        l=0
        r=len(nums)-1
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else: return 1

        while l<=r:
            mid= l+(r-l)//2
            if (mid+1<len(nums) and nums[mid]>nums[mid+1]) and (mid-1>=0 and nums[mid]>nums[mid-1]):
                return mid
            if nums[mid]< nums[mid+1]:
                l=mid+1
            else: r=mid-1
        

print(Solution.findPeakElement(1,[1,2,1,3,5,4]))