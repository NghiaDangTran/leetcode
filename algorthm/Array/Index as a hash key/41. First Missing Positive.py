class Solution:
    def firstMissingPositive(self, nums) -> int:
        container = [0]*len(nums)

        for i in nums:
            if 1<=(i)<=len(nums) :
                container[(i)-1] = -1
        print(container)
        for i in range(len(container)):
            if container[i] == 0:
                return i+1
        if nums[0]==1 and len(nums)==1:
            return 2
        return len(nums)+1

print(Solution.firstMissingPositive(1,[2,0,-1]))

[1,2,0]
