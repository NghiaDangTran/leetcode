



from copy import deepcopy


class Solution:
    def shoppingOffers(self, price, special, needs ) -> int:
        def checkOk(special,need):
            ok=[]
            for i in range(len(special)):
                add=True
                for j in range(len(need)):
                    if need[j]-special[i][j]<0:
                        add=False
                        break
                if add:
                    ok.append(i)
            return ok
                        

        def rec(price,special,need,currPrice):
            print(need)
            ans=checkOk(special,need)
            if len(ans)==0:
                for i in range(len(need)):
                    currPrice+=price[i]*need[i]

                top=currPrice
                currPrice=0
                return top
            nomore=0
            for i in need:
                if i==0:
                    nomore+=1
                if i<0:
                    
                    return 999999

            if nomore ==len(need)-1:
                return currPrice
            

            res= 999999
            print(need)
            for i in range(len(special)):
                add=True          
                for j in range(len(need)):
                    if need[j]-special[i][j]<0:
                        add=False
                        break
                
                if add:
                    for j in range(len(need)):
                        need[j]-=special[i][j]
                    
                    currPrice+=special[i][-1]

                    
                    ans=rec(price,special,need,currPrice)
                    res=min(res,ans)
                if add:
                    for j in range(len(need)):
                        need[j]+=special[i][j]
                    currPrice=0


            return res
        
        print(rec(price,special,needs,0))









Solution.shoppingOffers(1,price = [2,5], special = [[]], needs = [3,2])

           