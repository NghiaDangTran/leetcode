class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)-1
        def rec(lv,at,curr):
            
            if at<0 or at>n:
                return inf
            
            if lv==n:
                return matrix[lv][at]
            if (lv,at)in curr:
                return curr[(lv,at)]
            check=matrix[lv][at]+min(rec(lv+1,at-1,curr),rec(lv+1,at,curr),rec(lv+1,at+1,curr))
            
            curr[(lv,at)]=check
            
            return check
                
                
            
            
       
        res=99999
        for i in range(n+1):
            res=min(res,rec(0,i,{}))
        return res

                
        
        
        
    

        