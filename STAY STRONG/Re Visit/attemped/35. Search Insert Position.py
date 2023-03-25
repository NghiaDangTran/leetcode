class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
#         low = 0
#         high = len(nums) 
#         if target>max(nums):
#             return len(nums)
#         if target<=min(nums):
#             return 0
#         while low < high:
#             mid = low + (high - low) // 2
#             print(nums[mid])
           
            
#             if nums[mid] < target:
#                 low=mid+1

#             else:
#                 high = mid 

#         return low
        nums.append(target)
        nums.sort()
        return nums.index(target)
    
    
#      better solution 

#     nums.append(target)
#     nums.sort()
#     return nums.
    