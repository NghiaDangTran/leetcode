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
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start,end=0,0
        currWindow=0
        table={}
        while end!=len(s):
            if s[end] in table:
                table[s[end]]+=1
            else: table[s[end]]=1
            currWindow=max(currWindow,table[s[end]])
            # number of 1 char in the curr string start to end
            if (end-start)>=currWindow+k:
                
                table[s[start]]-=1
                
                start+=1
                        
            end+=1
            
            
        return end-start
            
            
            
# print(Solution.characterReplacement(1,"ABBBA"
# ,2))
# []
a="AABABBABBBABCCCCBACC"
from collections import Counter
table=Counter(a)
print(table.most_common())
