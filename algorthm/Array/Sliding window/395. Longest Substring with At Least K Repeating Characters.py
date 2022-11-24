class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        start, end, i = 0, 0, 0
        res = 0
        table = {}
        while end != len(s):

            table[s[end]] = table.get(s[end], 0)+1

            if s[end] != s[start]:
                print(table)
                temp = end+1
                strAtend = table[s[end]]
                strAtStand = table[s[start]]
                while temp < len(s) and (s[temp] == s[start] or s[temp] == s[end]):
                    if s[temp] == s[end]:
                        strAtend += 1
                    if s[temp] == s[start]:
                        strAtStand += 1
                    temp+=1
                print(strAtend,strAtStand)
                if strAtend >= k and strAtStand >= k:
                    table[s[end]] = strAtend
                    table[s[start]] = strAtStand
                    res = max(res, temp-start)
                    end = temp-1
                    flag=true,remer=res
                elif strAtend >= k and strAtStand < k:
                    while start != end-1:
                        table[s[start]] -= 1
                        if table[s[start]] == 0:
                            table.remove(s[start])
                    res = max(res, temp-end)
                    flag=true,remer=res
                    end = temp-1
                elif strAtend < k and strAtStand >= k:

                    res=max(end-start-1,res)
                    
                elif strAtend < k and strAtStand < k:
                    table = {}
                    end = temp-1

            end += 1

        return res


print(Solution.longestSubstring(1, "aaabb",
                                3))
