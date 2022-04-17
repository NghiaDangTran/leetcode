from unittest import result


class Solution:
    def minimumTotal(self, num) -> int:
        
        for i in range(len(num)-1,0,-1):
            
            for j in range(0,len(num[i])-1):
                num[i-1][j]+=min(num[i][j],num[i][j+1])
                
        print(num)

print(Solution.minimumTotal(1,[[2],[3,4],[6,5,7],[4,1,8,3]]))