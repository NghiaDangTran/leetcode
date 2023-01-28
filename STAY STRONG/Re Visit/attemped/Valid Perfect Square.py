class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=num
        
        while l<=r:
            mid=l+(r-l)//2
            # print(l,mid,r,mid*mid)
            if mid*mid==num:
                return True
            else:
                if mid*mid>num:
                    r=mid-1
                else:
                    l=mid+1
            
        return False
                
                    
        