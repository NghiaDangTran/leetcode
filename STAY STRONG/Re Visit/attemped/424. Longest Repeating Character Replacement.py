class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        table={}
        currmax=(0,0)
        res=0
        for i in range(len(s)):
            
            table[s[i]]=table.get(s[i],0)+1
            if currmax[0]<table[s[i]]:
                currmax=(table[s[i]],s[i])
            temp=currmax[0]+k
            temp2=i-l
            while  i-l>=currmax[0]+k:
                # print(currmax[0]+k)
                # res=max(currmax[0]+k,res)
                table[s[l]]-=1
                l+=1



                # table={}
            
        return i-l+1
            
        




print(Solution.characterReplacement(1,"AAA",k=2))