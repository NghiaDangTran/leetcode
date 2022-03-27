class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        count=0
        for i in nums:
            nums[count]=i*i
            count+=1
        nums.sort()
        return nums