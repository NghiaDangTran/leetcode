from typing import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

#         # basic idea path  
#         # s = "cbaebabacd"
#         # p = "abc"

#         # for i in range(s):
#         #     if s[i] in p:
#         #         remember the i 
#         #         while i<len(s) and s[i] in p and len(p)>0:
#         #             i++
#         #             p.remove(s[i])
#         #         if !p:
#         #             add remmber to the result:
#         # implement 

#         # result=[]
#         # i=0
#         # while i<len(s):
#         #     loc=0

#         #     temp=set(p)
#         #     if s[i] in temp:
#         #         loc=i
#         #         j=i
#         #         while j<len(s) and s[j] in temp and len(temp)>0:
#         #             temp=temp.replace(s[j],"",1)
#         #             j+=1
                
                
#         #         if len(temp)==0:
#         #             result.append(loc)
            
#         #     i+=1
#         #  this only work with average size data 
#         # not work with "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa" o(m*n)

#         # some reconise we dont attucally care the order in p or s
#         # dict may work here count every element in the current s length 
#           and for each value dict[s] - dict[p] then the new if the current dict equal 0 then add that to result
# usign count will work better in term of how hard to modify
            # result=[]
            # pCount=Counter(p)
            # for i in range(len(s)-len(p)+1):
            #     sCount=Counter(s[i:i+len(p)])
            #     if len(sCount-pCount)==0:
            #         result.append(i)
            # return result
            # this work but really slow 
            # better imorivement
            # so the sCounter will make our code slower
            # so if we think different we only need to del s[i] and then add the s[i+len(p)] into the counter
            result=[]
            pCount=Counter(p)
            sCount=Counter(s[:len(p)])
            
            for i in range(len(s)-len(p)+1):
                # print()
                if (pCount)==sCount:
                    result.append(i)
                sCount[s[i]]-=1
                if i+len(p)<len(s):
                    sCount[s[i+len(p)]]+=1
                
            return result
            

        










            
# # from typing import Counter


# # # temp="abc".counter()
# # print(Counter("abc")-Counter("abc"))
                
# print(dict("asd"))