class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        total=[]
        def generate(curr,op,cl):

            if op==n and cl==n:
                total.append(curr)
                return


            if cl<=op and op!=n:
                generate(curr+"(",op+1,cl)
            if  op!=cl:
                generate(curr+")",op,cl+1)
        generate("",0,0)
        return total



                    

        