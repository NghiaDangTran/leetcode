class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res={}
        def rec(nums,curr):
            res[''.join(str(x) for x in sorted(curr))]=curr

            for i in range(len(nums)):
                # curr.append(nums[i])
                # rec(nums[i+1:],curr)
                rec(nums[i+1:],curr+[nums[i]])

                # curr.pop(-1)

                # ''.join(xs)
        rec(nums,[])
        return list(res.values())