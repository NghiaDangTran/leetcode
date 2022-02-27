class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        curr=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else: i+=1
        return len(nums)

print(Solution().removeElement([0,1,2,2,3,0,4,2],2))

# Runtime: 27 ms, faster than 54.40% of Python online submissions for Remove Element.
# Memory Usage: 13.3 MB, less than 88.85% of Python online submissions for Remove Element.