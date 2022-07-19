


class Solution:
    def minNumberOperations(self, target) -> int:
        
        # first test case: [1,2,3,2,1]
        # naive idea is that pick the first value at i check i+1>i
        # if it is then add [i+1]-[i] to the result

        # but what happen when value at 0 is bigger than value at 1
        # let looks at the provided answer for [3,1,5,4,2]
        # [0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] ->
        #  [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2].
        #  notice that at stage 2 we INCREASING it first 
        # so that maybe we can set innitial result to be that value 
        # let try it 

        result=target[0]
        prev=target[0]

        for i in range(1,len(target)):
            if prev<target[i]:
                result+=target[i]-prev
            prev=target[i]
        return result

turn out it run ok. but how can we know our code is right when we have orther case?
because our solution not atually pick any value in any order so that 
greedy choice property is impossible to prove here