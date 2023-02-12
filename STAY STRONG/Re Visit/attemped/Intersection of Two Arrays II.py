class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res=[]
        
        for i in nums1:
            l,r=0,len(nums2)-1
            
            while l<=r:
                mid=l+(r-l)//2
                if nums2[mid]==i:
                    res.append(i)
                    nums2=nums2[:mid]+nums2[mid+1:]
                    break

                else:
                    if nums2[mid]<i:
                        l=mid+1
                    else: r=mid-1
        return res