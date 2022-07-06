class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        if sum(candidates)<target:
            return  []
        if sum(candidates)==target:
            return [candidates]
        
       
               

        def rec(data,currTarget,path):
            
            if currTarget==0:
                result.append(path)
                return

            if currTarget<0 :
                return
                
            for i in range(len(data)):
                if i>0 and data[i]==data[i-1]:
                    continue
                rec(data[i+1:],currTarget-data[i],path+[data[i]])

        rec(candidates,target,[])
        return result