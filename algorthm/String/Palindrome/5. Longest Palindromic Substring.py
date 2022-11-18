class Solution:
    def longestPalindrome(self, s: str) -> str:
        def Count_Palindrom(l,r):
           
            while l>=0 and r<len(s) and s[l]==s[r]:
                
                l-=1
                r+=1
            
            return s[l+1:r]
        res=""
        for i in range(len(s)):
            a,b=Count_Palindrom(i,i),Count_Palindrom(i,i+1)
            if len(res)<=len(a):
                res=a
            if len(res)<=len(b):
                res=b
        return res