class Solution:
    def threeSum(self, nums1) :
        
        
        result=[]
        nums1.sort()
        print(nums1)
        for i in range(len(nums1)-2):
            if i>0 and  nums1[i]==nums1[i-1]:
                continue
            # l=i-1
            # if l<0:

            #     l=0
            l=i+1
            r=len(nums1)-1

            while l<r:
                mid=nums1[l]+nums1[r]+nums1[i]
                
                if mid<0:
                    l+=1
                elif mid>0:
                    r-=1
                else:
                    result.append([nums1[l],nums1[r],nums1[i]])
                    while l<r and nums1[l]==nums1[l+1]:
                        l+=1
                    while l<r and nums1[r]==nums1[r-1]:
                        r-=1
                    l+=1
                    r-=1
            
        
            
        return result