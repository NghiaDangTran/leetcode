from collections import Counter

class Solution:
    def maxRepOpt1(self, s: str) -> int:
        c = Counter(s)
        start, end = 0, 0
        currWindow = 0
        table = {}
        currChar = ""
        res=0
        while end != len(s):
            if s[end] in table:
                table[s[end]] += 1
            else:
                table[s[end]] = 1
            # currWindow = max(currWindow, table[s[end]])
            if currWindow < table[s[end]]:

                currWindow = table[s[end]]
                currChar = s[end]
            print(currWindow,(end-start) > currWindow | end-start > c[currChar]-1)

            # number of 1 char in the curr string start to end
            while ((end-start) > currWindow) or end-start > c[currChar]-1:

                table[s[start]] -= 1

                start += 1
                for i in table:
                    if currWindow < table[i]:
                        currWindow = table[i]
                        

            res=max(res,end-start+1)
            end+=1
        return res
                
             
