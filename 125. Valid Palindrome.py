import re
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        test = ""
        for i in   re.sub('['+string.punctuation+']', '', s).split():
            test+=i
        
        
        
        if (len(test))%2!=0:
            left=right=len(test)//2
        else: 
            left=(len(test)-1)//2
            right=len(test)//2
        
        while left>=0:
            if(test[left]!=test[right]):
                return False
            left-=1
            right+=1
        return True


# Success
# Details 
# Runtime: 63 ms, faster than 59.47% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15.4 MB, less than 26.38% of Python3 online submissions for Valid Palindrome.