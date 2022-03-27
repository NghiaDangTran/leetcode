class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
   
        
     
  
        temp1=nums[(len(nums)-k)%len(nums):len(nums)]
        temp2=nums[0:(len(nums)-k)%len(nums)]
           
        print(temp1)
        print(temp2)
        temp1+=temp2
       
        nums[:]=temp1
#         this mean for i in range(len(nums))
      
        
        
        