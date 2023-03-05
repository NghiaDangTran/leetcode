class Solution:
    def restoreString(self, s: str, ind: List[int]) -> str:
        res=[""]*len(ind)
        for i in range(len(ind)):
            res[ind[i]]=s[i]
        return "".join(res)
        