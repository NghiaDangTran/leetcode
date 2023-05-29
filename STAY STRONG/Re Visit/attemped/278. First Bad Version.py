class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1
        
        low=0
        high=n-1

        while low<high:
            mid=  low + (high - low) // 2
            
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else: high=mid-1
            elif  isBadVersion(mid+1):
                    return mid+1
            else: low=mid+1
        return n
        