class Solution:
    def countHighestScoreNodes(self, parents) -> int:

        curr = [[] for _ in parents]
        for i, val in enumerate(parents):
            if val>=0:
                curr[val].append(i)

        
        table = {}

        def remove(val, arr):

            toremove = arr[val]
           

          
            currl = 0
            currr = 0

            if not len(toremove) == 0:
                at1 = remove(toremove[0], arr)
                currl = at1[0]+at1[1]+1
                if len(toremove)>1:
                  at2 = remove(toremove[1], arr)
                  currr = at2[0]+at2[1]+1
            
           
            freq=(currl or 1) * (currr or 1) * ((len(curr)-(currl+currr+1)) or 1)
            if table.get((freq),0)!=0:

                table[(freq)] += 1
            else:
                table[(freq)] = 1
            return [currl, currr]

        remove(0,curr)

        
        
        return table[max(list(table.keys()))]


print(Solution.countHighestScoreNodes(1, [-1,2,0,2,0]
))
