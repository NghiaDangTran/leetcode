from tkinter import S


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        print(s)
        
        for i in range(len(s)-1, 0, -1):
            
            if s[i]==" " or s[i]==0:
                return len(s)-i-1

        return len(s)

print(Solution.lengthOfLastWord(1," asdasd asd"))
