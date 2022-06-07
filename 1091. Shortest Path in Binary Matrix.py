class Solution:
    def shortestPathBinaryMatrix(self, data) -> int:
        if data[0][0]==1 or data[len(data)-1][len(data)-1]==1:
            return -1
        if len(data)==1 and data[0][0]==0:
            return 1

        allM = [[1,0], [-1,0], [0,1],[0,-1],[1,1], [-1,-1],[-1,1], [1,-1]]
        q = [(0,0,1)]
        data[0][0]=1
        # for i in allM:
        #     if 0+i[0] >= 0 and 0+i[0] < len(data) and 0+i[1] >= 0 and 0+i[1] < len(data) and data[0+i[0]][0+i[1]] == 0:
        #         q.append(( i[0], i[1], 1))

        
        # while q:
        #     currx,curry,path=q.pop(0)
        for currx,curry,path in q:
            if currx==curry==len(data)-1:
                return path
            for i in allM:
                if 0<= (currx+i[0])<len(data) and 0<= (curry+i[1])<len(data) and data[currx+i[0]][curry+i[1]]==0:
                    q.append(( currx+i[0], curry+i[1], path+1))
                    data[currx][curry]=1


      
            
        return -1

print(Solution.shortestPathBinaryMatrix(1,[[0,0,0],[1,0,0],[1,1,0]]

))

[[0,0,0],
[1,1,0],
[1,1,0]]
[[0,0,0],[0,1,0],[0,0,0]]
[0,0,0]
[0,1,0]
[0,0,0]

