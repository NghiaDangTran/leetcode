class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
    
        def dfs(data,curr):
            ret.append(curr)
            for i in range(len(data)):
                if i>0 and data[i]==data[i-1]:
                    continue
                dfs(data[i+1:],curr+[data[i]])
            
        dfs(nums,[])
        return ret