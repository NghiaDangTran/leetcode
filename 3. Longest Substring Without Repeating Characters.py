class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "abcabcbb"
        max1=0
        for i in range(len(s)):
            curr=s[i]
            for j in range(i+1,len(s)):
                if s[j] not in curr:
                    curr+=s[j]
                else: break
            
            max1=max(len(curr),max1)
        return (max1)


///
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=result=0
        data={}

        for i in range(len(s)):
            if s[i] not in data:
                result=max(result,i-l+1)
            else:
                if data[s[i]]>l:
                    l=data[s[i]]+1


            data[s[i]]=i