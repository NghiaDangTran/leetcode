class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        table=Counter(s)
        
        res=0
        for i in table.keys():
            
            for j in range(len(s)):
                if s[j]==i:
                    at=j+1
                    count=1
                    skip=k
                    while at<len(s) and (skip>0 or s[at]==i) :
                        if s[at]!=i:                            
                            skip-=1
                        
                        count+=1
                        at+=1
                    res=max(res,count)           
                    at=j-1
                    
                    while at>=0 and (skip>0 or s[at]==i) :
                        if s[at]!=i:                            
                            skip-=1
                        
                        count+=1
                        at-=1
                    res=max(res,count)
                    
                    
                
        return res

# print(Solution.characterReplacement(1,"ABBBA"
# ,2))
# []
a="AABABBABBBABCCCCBACC"
from collections import Counter
table=Counter(a)
print(table.most_common())
