class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return
        
        curr=0
        next=0
        while curr<len(nums):
            if nums[curr]==0:
                nums.pop(curr)
                next+=1

            else :curr+=1
            
        nums+=(next*[0])
            
            