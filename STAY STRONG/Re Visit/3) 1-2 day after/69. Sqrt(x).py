class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        r=x
        while l<=r:
            mid=l+(r-l)//2
            temp=mid*mid
            if mid*mid==x:
                return mid
            if mid*mid< x:
                l=mid+1
            else: r=mid-1
        return r

Solution.mySqrt(1,11)