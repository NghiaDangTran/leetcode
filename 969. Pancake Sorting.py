

class Solution:
    def pancakeSort(self, arr):
        n = len(arr)-1
        result = []
        while(n > 0):
            currMax = arr.index(max(arr[0:n+1]))
            #  if the pro Array is from 1-to length of array then we can replace the max with n
            

            if currMax == n:
                n -= 1

            else:
                if currMax != 0:
                    result.append(currMax+1)
                    arr = arr[currMax::-1]+arr[currMax+1:]

                else:
                    result.append(n+1)
                    arr = arr[n::-1]+arr[n+1:]

        return result


# res = []
#    for x in range(len(A), 1, -1):
#         print(A)

#         i = A.index(x)
#         res.extend([i + 1, x])
#         A = A[:i:-1] + A[:i]
#     return res


Solution.pancakeSort(1, [3, 2, 4, 1])

# original_list = [3, 2, 4, 1]
# at = 2
# original_list=original_list[at::-1]+original_list[at+1:]
# print(original_list)
# at = 3
# original_list=original_list[at::-1]+original_list[at+1:]
# print(original_list)
# at = 1
# original_list=original_list[at::-1]+original_list[at+1:]
# print(original_list)
# at = 2
# original_list=original_list[at::-1]+original_list[at+1:]
# print(original_list)
# at = 1
# original_list=original_list[at::-1]+original_list[at+1:]
# print(original_list)
