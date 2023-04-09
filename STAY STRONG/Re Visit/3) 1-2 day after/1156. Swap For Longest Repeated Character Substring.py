class Solution:
    def maxRepOpt1(self, text: str) -> int:
        curr={}
        for i in range(len(text)):
            curr[text[i]]=curr.get(text[i],0)+1


        l=0
        res=0
        skip=1
        for i in range(1,len(text)):
            if l<i and text[i]!=text[l]:

                r=i+1
                while r<len(text) and text[r]==text[l]:
                    r+=1
                res=max(r-l-1,res)
                if res<curr[text[l]]:
                    res+=1
                

                l=i
        if res==0:
            res=len(text)

        return res








print(Solution.maxRepOpt1(1, "aabaaba"))
