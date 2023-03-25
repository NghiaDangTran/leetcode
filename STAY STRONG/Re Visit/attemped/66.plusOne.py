class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        for i in range (len(digits)):
            s+=str(digits[i])

        s=int(s)+1
        result=[]
        for i in  str(s):
            result.append(int(i))
        return result

print(Solution.plusOne(1,[1,2,4,1]))