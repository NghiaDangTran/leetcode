# from ast import MatchAs


class Solution:
    # def updateMatrix(self, mat) :
        # data=[]
        # visted=[]
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j]==0:
        #             visted.append([i,j])
        #         else: data.append([i,j])
        # i=j=0
        # def processData(dataM,row,col):
           
        #     result=[]
        #     for i in range(len(dataM)):
        #         if dataM[i][0]==row :
        #             if abs(dataM[i][1]-col)==1:
        #                 return 1
        #             result.append(abs(dataM[i][1]-col))
        #         elif dataM[i][1]==col:
        #             if abs(dataM[i][0]-row)==1:
        #                 return 1
        #             result.append(abs(dataM[i][0]-row))
            
        #     return min(result)
        # while data:
        #     x,y=data.pop(0)
        #     mat[x][y]=processData(visted,x,y)

        # return mat
    def updateMatrix(self, mat) :
        data=[]
        visted=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    visted.append((i,j))
                    data.append((i,j))
                    
                
        i=0
        while data:
            row,col=data.pop(0)
           
            for i in [(0,1),(0,-1),(1,0),(-1,0)]:
                row1,col2=row+i[0],col+i[1]
                if row1>=0 and col2>=0 and row1<len(mat) and col2<len(mat[0]) and (row1,col2) not in visted:
                    mat[row1][col2]=mat[row][col] +1
                    visted.append((row1,col2))
                    data.append((row1,col2))
        return mat
                
                

        

print(Solution.updateMatrix(1,[[0,0,0],[0,1,0],[1,1,1]]))
# print("0,0,1,0,1,2,1,0,1,2\n1,1,2,1,0,1,1,1,4,5\n2,1,3,1,1,0,0,0,1,2\n1,0,1,0,1,1,1,0,1,2\n0,0,1,1,1,0,1,1,2,4\n1,0,1,2,1,1,1,2,1,4\n1,1,1,1,0,1,0,1,0,1\n0,1,0,0,0,1,0,0,1,2\n1,1,1,0,1,1,0,1,0,1\n1,0,1,1,1,0,1,2,1,0]]")
# print()

# print("0,0,1,0,1,2,1,0,1,2\n1,1,2,1,0,1,1,1,2,3\n2,1,2,1,1,0,0,0,1,2\n1,0,1,0,1,1,1,0,1,2\n0,0,1,1,1,0,1,1,2,3\n1,0,1,2,1,1,1,2,1,2\n1,1,1,1,0,1,0,1,0,1\n0,1,0,0,0,1,0,0,1,2\n1,1,1,0,1,1,0,1,0,1\n1,0,1,1,1,0,1,2,1,0")
# [0,0,1,0,1,1,1,0,1,1]
# [1,1,1,1,0,1,1,1,1,1]
# [1,1,1,1,1,0,0,0,1,1]
# [1,0,1,0,1,1,1,0,1,1]
# [0,0,1,1,1,0,1,1,1,1]
# [1,0,1,1,1,1,1,1,1,1]
# [1,1,1,1,0,1,0,1,0,1]
# [0,1,0,0,0,1,0,0,1,1]
# [1,1,1,0,1,1,0,1,0,1]
# [1,0,1,1,1,0,1,1,1,0]



