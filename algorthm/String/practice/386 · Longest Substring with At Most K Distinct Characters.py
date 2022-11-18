
# Description
# Given a string S, find the length of the longest substring T that contains at most k distinct characters.

# Wechat reply 【Google】 get the latest requent Interview questions. (wechat id : jiuzhang0607)


# Example
# Example 1:

# Input: S = "eceba" and k = 3
# Output: 4
# Explanation: T = "eceb"
# Example 2:

# Input: S = "WORLD" and k = 4
# Output: 4
# Explanation: T = "WORL" or "ORLD"
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        start,end=0,0
        currWindow=0
        res=0
        temp=0
        table={}
        while end!=len(s):
            
            if table.get(s[end],0)==0:
                currWindow+=1
            table[s[end]]+=1
            while currWindow>k:
                # print(table,start,currWindow,[s[start]])
                if table[s[start]]==1:
                    currWindow-=1           
                table[s[start]]-=1
                start+=1
            res=max(res,end-start+1)      
            end+=1
        
       
        return res
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        start,end=0,0
        currWindow=0
        res=0
        temp=0
        table={}
        while end!=len(s):
            
            
            table[s[end]]=table.get(s[end],0)+1
            while len(table)>k:
                # print(table,start,currWindow,[s[start]])
                if table[s[start]]==1:
                    table.pop(s[start], None)
                    start+=1
                    break
                    
                table[s[start]]-=1
                start+=1
            res=max(res,end-start+1)
            
            end+=1
        return res
print(Solution.length_of_longest_substring_k_distinct(1,"eceebeabcaasdcczxsadeeeeeeeaaaaaaaaaaaaaccccccccccccccccccccdddddddddddddddddddddd",3))
