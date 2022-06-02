# class Solution:
#     def findCircleNum(self, data) -> int:
#             pos=list(range(len(data)))
#             res=[]
#             while pos:
#                 i=pos.pop()
#                 stack=[]
#                 prov=[]
#                 stack.append(i)
#                 prov.append(i)
#                 while stack:
#                     i=stack.pop()
#                     for j in range(len(data)):
#                         if i!=j and data[i][j]==1:
#                             if j not in prov:
#                                 stack.append(j)
#                                 pos.remove(j)
#                                 prov.append(j)
#                 res.append(prov)
#             return len(res)
            
# work but need to improve speed

class Solution:
    def findCircleNum(self, data) -> int:
            pos=list(range(len(data)))
            res=0
            while pos:

                i=pos.pop()

                res+=1
                stack=[]
                stack.append(i)
                while stack:
                    i=stack.pop()
                    for j in range(len(data)):
                        if i!=j and data[i][j]==1:
                            if j  in pos:
                                stack.append(j)
                                pos.remove(j)
            return res
print(Solution.findCircleNum(1, [[1,1,0],[1,1,0],[0,0,1]]))


# pos=[] lambda i: :
# res=[]
# while pos:
#     prov=[]
#     stack=[]
#     i=pos.pop()
#     prov.append(i)

#     stack.append(i)
    
#     while stack:
#         i=stack.pop()
#         for j in range(len(data)):
#             if i!=j and data[i][j]==1 :
#                 if j not in stack:
#                     stack.append(j)
#                     pos.remove(j)
#                     if j not in prov:
#                         prov.append(j)
#     res.append(prov)
# return len(res)
