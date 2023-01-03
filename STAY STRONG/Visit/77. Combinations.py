import copy
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res1=[]
        all=[i for i in range(1,n+1)]
        # print(n)
        def p_combine(all,k,curr):


            if len(curr)==k:
                temp=copy.deepcopy(curr)
                
                res1.append(temp)

                return 
            for i in range(len(all)):
                curr.append(all[i])
                p_combine(all[i+1:],k,curr)
                curr.pop(-1)


           

                

        p_combine(all,k,[])
        return res1


            

                
            


        