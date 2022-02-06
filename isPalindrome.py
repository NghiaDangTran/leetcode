class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        test=str(x)
        
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