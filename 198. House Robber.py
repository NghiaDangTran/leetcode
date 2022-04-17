class Solution:
    def rob(self, nums1: List[int]) -> int:
        data=[0,nums1[0]]
        for i in range(1,len(nums1)):
            data.append(max(data[i],data[i-1]+nums1[i]))
        return data[-1]
        
#         data=[]
#         def rec(nums,at):
#             if at<0:
#                 return 0
#             result= max(nums[at]+rec(nums,at-2),rec(nums,at-1))
#             data.append(result)
#             return result
#         rec(nums1,len(nums1)-1)
#         print(data)
        
#         return data[-1]
            