class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        def rec(nums,curr):


            res.append(curr)
            for i in range(len(nums)):
                # curr.append(nums[i])
                # rec(nums[i+1:],curr)
                rec(nums[i+1:],curr+[nums[i]])

                # curr.pop(-1)
        rec(nums,[])
        return res