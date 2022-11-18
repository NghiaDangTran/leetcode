class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
				101]
        res={}

        for i in strs:
            check=1
            for j in i:
                check*=ord(i)-97
            
            if check in res:
                res[check].append(i)
            else: res[check]=[i]
        
        return res.values