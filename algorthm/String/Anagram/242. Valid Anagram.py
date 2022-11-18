class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def sortString(str) :
            str = ''.join(sorted(str))
            return str
        return sortString(s)==sortString(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        if len(s)!=len(t):
            return False
        
        for i in s:
            if i in dic:
                dic[i]+=1
            else: dic[i]=1
        
        for i in t:
            
            if i in dic:
                if dic[i]==0:
                    return False
                dic[i]-=1
            else: return False
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
				101]
        a=1
        for i in s:
            a*=table[(ord(i)-97)]
        b=1
        for i in t:
            b*=table[(ord(i)-97)]
   

        return a==b