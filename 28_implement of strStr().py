class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.append(target)
        nums.sort()
        return nums.index(target)
        
    
    
    
    
    
    def binarySearch(arr, l, r, x):
    
        # Check base case
        if r >= l:
        
            mid = l + (r - l) // 2
    
            # If element is present at the middle itself
            if arr[mid] == x:
                return mid
    
            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif arr[mid] > x:
                return Solution.binarySearch(arr, l, mid-1, x)
    
            # Else the element can only be present
            # in right subarray
            else:
                return Solution.binarySearch(arr, mid + 1, r, x)
    
        else:
            # Element is not present in the array
            return -1