class Solution:
    def longestNiceSubstring(self, s: str) -> str:


     

        def rec(s):
            
                
            data = set(s)
            flag=True
            for i in range(len(s)):
                if s[i].swapcase() not in data:
                    s0=rec(s[:i])
                    s1=rec(s[i+1:])
                    print(max(s0, s1, key=len))
                    return max(s0, s1, key=len)
            return s
                # result=s
                # normal i can set the result right here but string is immutable so have to make to array
                
       

        return  rec(s)