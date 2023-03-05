class Solution:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]

        def searchL():
            l = 0
            r = len(nums)-1

            while l <= r:
                mid = l+(r-l)//2

                if nums[mid] >= target:
                    r = mid-1
                else:
                    l = mid+1
            return l


        def searchR():
            l = 0
            r = len(nums)-1

            while l <= r:
                mid = l+(r-l)//2

                if nums[mid] >target:
                    r=mid-1
                else:
                    l = mid+1
            return r

        if searchR()<searchL():
            return [-1,-1]
        return [searchL(), searchR()]
Solution.searchRange(1,[5,7,7,8,8,10],6)
