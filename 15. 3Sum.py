class Solution:
    def threeSum(self, nums1) :
        
        if len(nums1)<=2:
            return []
        nums1.sort()
        print(nums1)
        result=[]

        def t2(nums,target,at):
           
            i = 0
            j = len(nums) - 1
            # print(nums)
            while(i<j):
                if nums[i]+nums[j]+target==0:
                    # result.append([nums[i+1],nums[j+1],target])
                    if sorted([nums[i],nums[j],target]) not in result:
                        result.append(sorted([nums[i],nums[j],target]))
                    return
                if nums[i]+nums[j]>target:
                    j-=1
                else: i+=1
            
            
        
        for i in range(len(nums1)-1,-1,-1):
            t2(nums1,-1*nums1[i],i)
            # print(nums1[0:i]+nums1[i+1:len(nums1)])
        return result


[0,2,7,11,15],9
    