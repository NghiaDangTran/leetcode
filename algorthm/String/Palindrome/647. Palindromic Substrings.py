

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j+1]==s[i:j+1][::-1]:
                    
                    res += 1
        return res

class Solution:
    def countSubstrings(self, s: str) -> int:
        def Count_Palindrom(l,r):
            res=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res
        res=0
        for i in range(len(s)):
            res+=Count_Palindrom(i,i)
            res+=Count_Palindrom(i,i+1)
        return res


print(Solution.countSubstrings(1, "aaacaa"))
