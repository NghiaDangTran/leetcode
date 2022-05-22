from ctypes import pointer


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        # 2 pointer

        l = 0
        pro = 1
        res = 0
        for r in range(len(nums)):
            pro *= nums[r]

            while pro >= k and l<=r:
                pro //= nums[l]
                

                l += 1
           
        #    at the end of the while the left 
# the importance thing here is that we need to calculate the r-l+1
    # the logic is when ever the pro bigger than the k then we will do the l+1
            res += r-l+1
        return res


print(Solution.numSubarrayProductLessThanK(1, [1, 2, 3], 0))
