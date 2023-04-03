class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        stack = [(sr, sc)]
        result = []
        while stack:
            curr = stack[0]
            if curr not in result:
                result.append(curr)

            stack.pop(0)
           
            if curr[0]+1<=len(image)-1:
                if ((curr[0]+1, curr[1]) not in result) and image[curr[0]+1][curr[1]] == image[curr[0]][curr[1]]:
                    
                    stack.append((curr[0]+1, curr[1]))
                    result.append((curr[0]+1, curr[1]))
            if curr[0]-1>=0:
                if ((curr[0]-1, curr[1]) not in result) and image[curr[0]-1][curr[1]] == image[curr[0]][curr[1]]:
                    

                    stack.append((curr[0]-1, curr[1]))
                    result.append((curr[0]-1, curr[1]))
            if curr[1]+1<=len(image[0])-1:
                if ((curr[0], curr[1]+1) not in result) and image[curr[0]][curr[1]+1] == image[curr[0]][curr[1]]:
                    stack.append((curr[0], curr[1]+1))
                    result.append((curr[0], curr[1]+1))
            if curr[1]-1>=0:
                if ((curr[0], curr[1]-1) not in result) and image[curr[0]][curr[1]-1] == image[curr[0]][curr[1]]:
                    stack.append((curr[0], curr[1]-1))
                    result.append((curr[0], curr[1]-1))
            print(stack)
        
        for i, j in result:
            image[i][j] = newColor
        return image

print(Solution.floodFill(1, [[1, 1, 1], [1, 1, 0]], 1, 1, 2))
