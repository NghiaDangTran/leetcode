class Solution(object):
    def removeDuplicates(self, data):
        """
        :type nums: List[int]
        :rtype: int
        """
        if data == [] or len(data) == 1:
            return len(data)

        data.sort()
        
        i=0
        while i<len(data)-1:
            
            if data[i] == data[i+1]:
                

                data.pop(i)
            else:
                
                i+=1
        return len(data)
    
#Runtime: 158 ms, faster than 18.89% of Python online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 14.4 MB, less than 96.23% of Python online submissions for Remove Duplicates from Sorted Array.
