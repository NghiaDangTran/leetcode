class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # table={}

        # for i in nums:
        #     if i in table:
        #         return i
        #     else:
        #         table[i]="1"
        # temp=nums
        # temp.sort()
        
        # total posible number in array is from 1 to n
        # then if each value stay for positional then make then negative
        # the next time we come to that postion the data will negative duplitate 
        
        for i in nums:
            if nums[abs(i)]<0:
                return abs(i)
            else: nums[abs(i)]=nums[abs(i)]*-1



