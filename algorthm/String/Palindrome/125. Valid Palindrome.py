class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        test = ""
        for i in   re.sub('['+string.punctuation+']', '', s).split():
            test+=i
   
        l,r=0,len(test)-1
        
        while(l<r):
            if test[l]!=test[r]:
                return False
            l+=1
            r-=1
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        test = ""
        for i in   re.sub('['+string.punctuation+']', '', s).split():
            test+=i
        return test==test[::-1]
        


