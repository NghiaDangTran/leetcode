# import math
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         # dynamic program
#         # nums = [10,5,2,6], k = 100
#         # idea for i in range of nums 
#         # i go from 0 to end
#         curr=0
#         for i in range(len(nums)):
#             temp=nums
#             for j in range(i):

            
#         return 0
        
# nums = [10,5,2,6]
# k = 100
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
import math

class Solution(object):
    def subsets(self, nums,k):
        ret = []
        
    
        def dfs(data,curr):
            if math.prod(curr)<k:
                ret.append(curr)
            for i in range(len(data)):
                dfs(data[i+1:],curr+[data[i]])
            
        dfs(nums,[])
        ret.sort()
        return ret

print(Solution.subsets(1, [10,5,2,6],100))

# print([3]+[1,2])