class Solution:

    def maxAreaOfIsland(self, grid) -> int:
        def floodFill(self, image, sr: int, sc: int):
            stack = [(sr, sc)]
            result = []
            result.append(stack[0])

            while stack:
                curr = stack[0]

                stack.pop(0)

                if curr[0]+1 <= len(image)-1:
                    if ((curr[0]+1, curr[1]) not in result) and image[curr[0]+1][curr[1]] == image[curr[0]][curr[1]]:

                        stack.append((curr[0]+1, curr[1]))
                        result.append((curr[0]+1, curr[1]))
                if curr[0]-1 >= 0:
                    if ((curr[0]-1, curr[1]) not in result) and image[curr[0]-1][curr[1]] == image[curr[0]][curr[1]]:

                        stack.append((curr[0]-1, curr[1]))
                        result.append((curr[0]-1, curr[1]))
                if curr[1]+1 <= len(image[0])-1:
                    if ((curr[0], curr[1]+1) not in result) and image[curr[0]][curr[1]+1] == image[curr[0]][curr[1]]:
                        stack.append((curr[0], curr[1]+1))
                        result.append((curr[0], curr[1]+1))
                if curr[1]-1 >= 0:
                    if ((curr[0], curr[1]-1) not in result) and image[curr[0]][curr[1]-1] == image[curr[0]][curr[1]]:
                        stack.append((curr[0], curr[1]-1))
                        result.append((curr[0], curr[1]-1))

            return result
        total_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total_island=max(total_island,len(floodFill(1, grid, i, j)))
        return (total_island)


class Solution:
    def maxAreaOfIsland(self, grid) -> int:

        def dfs(grid, row, col):
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[row]) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            print(grid)

            return (1 + dfs(grid, row + 1, col) + dfs(grid, row - 1, col) + dfs(grid, row, col + 1) + dfs(grid, row, col - 1))
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    print(dfs(grid, i, j))
                    result = max(result, dfs(grid, i, j))


print(Solution.maxAreaOfIsland(1, [[1, 1, 0, 0, 0], [
      1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
