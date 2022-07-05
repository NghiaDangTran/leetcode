class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        


        def rec(data,currTarget,path):
                     
            if currTarget==0:
                result.append(path)
                return

            if currTarget<0:
                return
                
            for i in range(len(data)):
                
                rec(data[i:],currTarget-data[i],path+[data[i]])

        rec(nums,target,[])
        return result