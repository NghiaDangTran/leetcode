class Solution:

    def twoSum(self, nums, target: int) :
        # nums= sorted(set(nums), key=nums.index)
        # print(nums)
        #         data={}
        #         for i in range(len(nums)):
        #             find=target-nums[i]
        #             # if find in nums[i+1:]:
        #             if nums[i] in data:
        #                 return [data[nums[i]]+1,i+1]
        #             data[find]=i
        i = 0
        j = len(nums) - 1
        while(i<j):
            if nums[i]+nums[j]==target:
                return [i+1,j+1]
            if nums[i]+nums[j]>target:
                j-=1
            else: i+=1
            
