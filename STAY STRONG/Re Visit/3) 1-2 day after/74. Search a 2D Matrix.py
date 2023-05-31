class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        l = 0
        r = (len(matrix))*(len(matrix[0]))-1
       

        while l<=r:
            mid = l+(r-l)//2
            row = mid // (len(matrix[0]))
            col = mid % (len(matrix[0]))
           
            if matrix[row][col]==target:
                return True
            if matrix[row][col]>target:
                r=mid-1
            else: l=mid+1
        # matrix[1,1]
        return False



print(Solution().searchMatrix(
   [[1,3,5,7,8],[10,11,16,20,21],[23,30,34,60,70]],100))
