from copy import deepcopy
import random


class Solution:
    
    
    def findKthLargest(self, nums, k: int) -> int:
        a=deepcopy(nums)
        a.sort()
        print(a[::-1])
        
        def quickSelect(arr,low,high,k):
            curr= partition(arr, low, high)
            
            # k go from first (0) ,second (1) so k need k-1
            if curr==k-1:
                return arr[curr]
            if curr>=k:
                return quickSelect(arr,low,curr-1,k)
            return quickSelect(arr,curr+1,high,k)
        
        
        def partition(array, low, high):
  
 
          pivot = array[high]

          i = low 


          for j in range(low, high):
            if array[j] >pivot:



              (array[i], array[j]) = (array[j], array[i])
              i = i + 1



          (array[i ], array[high]) = (array[high], array[i])

          return i 

        return quickSelect(nums, 0, len(nums)-1,k)


print(Solution.findKthLargest(1,[random.randint(-5,5) for i in range(9)],2))
print(Solution.findKthLargest(1,[random.randint(-5,5) for i in range(10)],2))
print(Solution.findKthLargest(1,[random.randint(-5,5) for i in range(2)],2))
print(Solution.findKthLargest(1,[random.randint(-5,5) for i in range(3)],2))
print(Solution.findKthLargest(1,[random.randint(-5,5) for i in range(5)],2))
print(Solution.findKthLargest(1,[random.randint(-5,5) for i in range(6)],2))
# [3,2,1,5,6,4]
# [5,2,1,3,6,4] i=1
# [5,6,1,3,2,4] i=2
# [5,6,4,3,2,1] i=3


# [6,5,4,3,1,2]
