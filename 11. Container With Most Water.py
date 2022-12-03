class Solution:
    def maxArea(self, data: List[int]) -> int:
        l=0
        r=len(data)-1
        currMax=0
        
        while l<r:
            print(l,r)
            if (min(data[l],data[r])*abs(l-r))>currMax:
                
                currMax=min(data[l],data[r])*abs(l-r)
            if data[l]<data[r]:
                l+=1
            else:
                r-=1
        
        
        return currMax


