
class Solution(object):
    def subsets(self, nums,k):
        ret = []
        
    
        def dfs(data,curr):
           
            ret.append(curr)
            for i in range(len(data)):
                dfs(data[i+1:],curr+[data[i]])
            
        dfs(nums,[])
        return ret

print(Solution.subsets(1, [10,5,2,6],100))