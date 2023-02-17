
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # direction=[(0,1),(1,0),(-1,0),(0,-1)]
        # curr=(0,0)
        # res=[matrix[curr[0][curr[1]]]

        # while curr[0]!=len(matrix) and curr[1]!=len(matrix[0]):
        #     if matrix[curr[0]][curr[1]]!=-1 and  curr[1]+direction[0][1]<len(matrix):
        #         curr=(curr[0],curr[1]+direction[0][1])
        #         res.append(matrix[curr[0][curr[1]])
        #         matrix[curr[0]][curr[1]]=-1

        #     if matrix[curr[0]][curr[1]]!=-1 and  curr[1]+direction[0][1]>=0:

        #         curr=(curr[0],curr[1]+direction[0][1])
        #         res.append(matrix[curr[0][curr[1]])
        #         matrix[curr[0]][curr[1]]=-1
        #     if matrix[curr[0]][curr[1]]!=-1 and  curr[0]+direction[0][0]<len(matrix[0]):
        #         move 2 down
        #     if matrix[curr[0]][curr[1]]!=-1 and  curr[0]+direction[0][0]>=0:
        #         move 2 up
        #     else:
        x, y = 0, 0
        res = [matrix[x][y]]
        matrix[x][y] = 999
        while True:
            while y+1 < len(matrix[0]) and matrix[x][y+1] != 999:
                    y += 1
                    res.append(matrix[x][y])
                    matrix[x][y] = 999

            else:
                while x+1 < len(matrix) and matrix[x+1][y] != 999:
                    x += 1
                    res.append(matrix[x][y])
                    matrix[x][y] = 999
                else: 
                    while  y-1>=0 and matrix[x][y-1]!=999 :
                        y-=1
                        res.append(matrix[x][y])
                        matrix[x][y]=999
                    else: 
                        while  x-1>=0 and matrix[x-1][y]!=999 :
                            x-=1
                            res.append(matrix[x][y])
                            matrix[x][y]=999
            
                        else: break
        
        return res




