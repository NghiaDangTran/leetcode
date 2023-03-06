class Solution:
    def canSeePersonsCount(self, h: List[int]) -> List[int]:
        res=[0]*len(h)
        stack=[(len(h)-1,h[-1])]
        for i in range(len(h)-2,-1,-1):

            while stack and h[i]>stack[-1][1]:
                stack.pop()
                res[i]+=1

            if stack:
                res[i]+=1
            stack.append((i,h[i]))
        return res