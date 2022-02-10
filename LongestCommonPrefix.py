    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=""
        i=1
        j=0
        while result != strs[0]:
            curr=strs[0][j]
            for i in range(len(strs)):
                if j>len(strs[i])-1  or strs[i][j]!=curr:
                    return result
            result+=curr
            j+=1                    
        return result
print(longestCommonPrefix(1,["ab", "a"]))
