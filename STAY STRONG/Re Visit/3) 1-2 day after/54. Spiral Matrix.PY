class Solution:
    def spiralOrder(self, matrix):

        x,y=0,0
        res=[matrix[x][y]]
        matrix[x][y]=999


        while True:
            while y+1<len(matrix[0])  and matrix[x][y+1]!=999:
                y+=1

                res.append(matrix[x][y])
                matrix[x][y]=999


            while x+1<len(matrix) and matrix[x+1][y]!=999 :
                x+=1
                res.append(matrix[x][y])
                matrix[x][y]=999

            while y-1>=0  and matrix[x][y-1]!=999:
                y-=1

                res.append(matrix[x][y])
                matrix[x][y]=999

            
            while x-1>=0 and matrix[x-1][y]!=999:
                x-=1
                res.append(matrix[x][y])
                matrix[x][y]=999
                
                

            
            if len(res)==len(matrix)*len(matrix[0]):
                return res
            
print(Solution.spiralOrder(1, [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))


        