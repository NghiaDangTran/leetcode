# #  naive thinking
# # from numpy import array


# class Solution:
#     def searchMatrix(self, matrix, target: int) -> bool:
#         # thinking of what we have on hand: len of array, len of array[i]
#         # so if we go into each of the len(array) call i if array[i][0]<=target<= array[i][len(array[i])]
#         # then apply the binary search in the array[i]
#         def binarysearch(data, at):
#             l = 0
#             r = len(data)-1
#             while l <= r:
#                 mid = l+(r-l)//2
#                 if data[mid] == at:
#                     return True
#                 elif data[mid] < at:
#                     l = mid + 1

#                 else:
#                     r = mid - 1
#             return False
#         # naive finish
#         # for i in range(len(matrix)):
#         #     if matrix[i][0] <= target <= matrix[i][len(matrix[i])-1]:
#         #         return binarysearch(matrix[i], target)

#         # improved by apply binary seach into the loop
#         l = 0
#         r = len(matrix)-1

#         while l <= r:
#             mid = l+(r-l)//2
#             if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid])-1]:
#                 return binarysearch(matrix[mid], target)
#             elif matrix[mid][0] < target:
#                 l = mid+1
#             else:
#                 r = mid-1
        
#         return False

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # optimal solutoin think the array like an atutally 1 long array annd just use binary search on it
        
        row=len(matrix)
        col=len(matrix[0])
        l=0
        r=row*col-1

        while l<=r:
            mid= (l+r)//2
            at=matrix[mid//col][mid%col]
            if at==target:
                return True
            if at<target:
                l=mid+1
            else:
                r=mid-1
        return False


print(Solution.searchMatrix(1, [[1]], 13))

print(0+(11-0)//2)
print(5//3)
print(5%4)