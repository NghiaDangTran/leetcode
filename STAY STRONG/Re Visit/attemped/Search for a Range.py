# class Solution:
#     def searchRange(self, nums: List[int], t: int) -> List[int]:
#         l = 0
#         mid = -1
#         r = len(nums)-1
#         while l <= r:
#             while l < len(nums)-1 and nums[l] == nums[l+1]:
#                 l += 1
#             while r > 0 and nums[r] == nums[r-1]:
#                 r -= 1

#             mid = l+(r-l)//2
#             if nums[mid] == t:
#                 break
#             if nums[mid] < t:
#                 l = mid+1
#             else:
#                 r = mid-1
#         l = -1
#         r = -1
#         if mid != -1 and nums[mid] == t:
#             l = mid
#             while l > 0 and nums[l-1] == t:
#                 l -= 1
#             r = mid
#             while r < len(nums)-1 and nums[r+1] == t:
#                 r += 1
#             print(l, r)
#         return [l, r]


def search_range(nums, target):
    def binary_search_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid =left+ ( right-left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def binary_search_right(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid =left+ ( right-left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = binary_search_left(nums, target)
    if left_index == len(nums) or nums[left_index] != target:
        return [-1, -1]
    right_index = binary_search_right(nums, target)
    print([left_index, right_index])
    return [left_index, right_index]
search_range([5,7,7,8,8,10],8)