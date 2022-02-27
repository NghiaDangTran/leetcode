class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        curr1 = 0
        curr2 = 0


        for i in range(m+n):
            if nums1[i]==0 and curr2<n:
                nums1[i]=nums2[curr2]
                curr2+=1

        nums1.sort()

        


        return nums1