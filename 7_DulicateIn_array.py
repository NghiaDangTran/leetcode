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