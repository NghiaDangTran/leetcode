class Solution:
    def numIslands(self, grid) -> int:
        res=0
        table={
        }
        direction=[(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print("a")
                if table.get(f"{i}_{j}",0)==0 and grid[i][j]=="1": 
                    res+=1               
                    stack=[(i,j)]
                    table[f'{i}_{j}']=1

                    
                    while stack:
                        currx,curry=stack.pop()
                        for x,y in direction:
                            tempx=currx+x
                            tempy=curry+y
                            if tempx>=0 and tempx<len(grid) and tempy>=0 and tempy<len(grid[0]) and grid[tempx][tempy]=="1" and table.get(f"{tempx}_{tempy}",0)==0:
                                stack.append((tempx,tempy))
                                table[f'{tempx}_{tempy}']=1
        return res
    
print(Solution.numIslands(1,[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
))



