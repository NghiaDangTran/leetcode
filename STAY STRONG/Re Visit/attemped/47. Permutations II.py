class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def rec(data,curr):
            if not data:
                result.append(curr)
            
            for i in range(len(data)):
                if i>0 and data[i]==data[i-1]:
                    continue
                rec(data[:i]+data[i+1:],curr+[data[i]])

        rec(nums,[])
        return result