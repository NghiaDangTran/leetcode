class Solution:
    def minWindow(self, s: str, t: str) -> str:
        table = {}
        for i in t:
            table[i] = table.get(i, 0)+1
        
        contain = len(t)
        begin = 0
        
        at1,at2=0,0
        for i in range(len(s)):
            if s[i] in table:
                table[s[i]] -= 1
                if table[s[i]] == 0:
                    contain -= 1
                # stack.append(i)
            if contain == 0:
                # or table[s[begin]]<0
                while ( s[begin] not in table or  table[s[begin]]<0 ) :
                   
                    if s[begin] in table:
                        table[s[begin]] += 1
                        
                        
                            
                        
                    
                    begin += 1
                
                if not at1 or i+1-begin<=i+1-at1:
                    at1,at2=begin,i+1

        
        if at1==at2:
            return ""

        return s[at1:at2+1]


print(Solution.minWindow(1, "ADOBECODEBANC", "ABC"))
