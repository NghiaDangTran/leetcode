class Solution:
    def minimumTotal(self, triangle) -> int:
        n=len(triangle)
        table=[]
        coptb=[[-9999]*i for i in range(1,n+1)]


        def calRec(curr,res,lv):
            print(lv,n)

            if lv==n:
                
                table.append(res)
                # coptb[lv-1][curr]=res
                return res
            if coptb[lv][curr]!=-9999:
                return coptb[lv][curr]
            coptb[lv][curr]=min(calRec(curr+1,res+triangle[lv+1][curr+1],lv+1),calRec(curr,res+triangle[lv+1][curr],lv+1))
            print(coptb[lv][curr],lv,curr)
            return coptb[lv][curr]

            
        
        
        return calRec(0,triangle[0][0],0)
print(Solution.minimumTotal(1,[[2],[3,4],[6,5,7],[4,1,8,3]]))