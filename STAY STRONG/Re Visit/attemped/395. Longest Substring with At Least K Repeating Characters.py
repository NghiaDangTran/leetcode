class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def isValid(start,end,table,unique):
            curr=list(table.keys())
            currK=0
            for i in range(len(curr)):
                if table[curr[i]]>=k:
                    currK+=1
            return currK==unique
        result=0
        for i in range(len(s)):
            table={}
            unique=0
            for j in range(i,len(s)):
                if(table.get(f"{s[j]}",0)==0):
                    unique+=1

                table[f"{s[j]}"]=table.get(f"{s[j]}",0)+1
                if isValid(i,j,table,unique):
                    result=max(result,j-i+1)
        return result
                
            



           




