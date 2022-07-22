class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        data={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],

        }
        contain=[]
        result=[]
        for i in range(len(digits)):
            contain.append(data[digits[i]])
        
        
        
        
        

        def rec(memo,curr,currlv):
            
            if currlv==len(contain):
                result.append(curr)
                return
            
            for i in range(len(memo[currlv])):
                
                
                rec(memo,curr+memo[currlv][i],currlv+1)
        
        
        rec(contain,"",0)
        return result
      