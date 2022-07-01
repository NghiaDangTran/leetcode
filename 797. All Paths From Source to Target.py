class Solution:
    def allPathsSourceTarget(self, graph) :
        
        result=[]
        def recGo(path,arr,curr):
            for i in arr:
                temp=curr+[i]
                if i==len(graph)-1:
                    result.append(temp)
                else:
                    recGo(i,graph[i],temp)
        
        recGo(0,graph[0],[0])
        return(result)

Solution.allPathsSourceTarget(1,[[4,3,1],[3,2,4],[3],[4],[]])
