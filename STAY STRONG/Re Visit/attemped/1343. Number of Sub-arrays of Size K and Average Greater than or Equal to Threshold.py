class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:

        # res = 0
        # i = 1
        # at = sum(arr[0:k])
        # if at/k >= threshold:
        #     res += 1
        # while i <= len(arr)-k:

        #     at += arr[i+k-1]-arr[i-1]

        #     if at/k >= threshold:
        #         res += 1
        #     i += 1
        # return res
        res = 0
        curr=sum(arr[0:k])
        if curr/k>=threshold:
            res+=1
        for i in range(k,len(arr)):
            curr+=arr[i]-arr[i-k]
            if curr/k>=threshold:
                res+=1
        
        return res
print(Solution.numOfSubarrays(1, [2,2,2,2,5,5,5,8], 3, 4))


print(Solution.numOfSubarrays(1, [11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
[2,2,2,2,5,5,5,8]
3
4



