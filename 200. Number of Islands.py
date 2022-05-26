class Solution:
    def numIslands(self, grid) -> int:

        def dfs(grid, row, col):
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[row]) or grid[row][col] == "0":
                return 
            grid[row][col] = "0"
#              mark this as already move
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)


            # return (1 + dfs(grid, row + 1, col) + dfs(grid, row - 1, col) + dfs(grid, row, col + 1) + dfs(grid, row, col - 1))
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    
                    result+= 1
        return result


print(Solution.numIslands(1, [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))