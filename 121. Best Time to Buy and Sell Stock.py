from cgi import print_environ


class Solution:

    def maxProfit(self, prices) -> int:
        
        if len(prices)==1 or len(prices)==0:
            return 0 
    
        i=0 
        # buy
        j=1
        #  sell
        currmax=0
        while j<len(prices):
            print(i,j)
            currmax=max(currmax,prices[j]-prices[i])
            if prices[i]>prices[j]:
                i=j
            j+=1

            


            

        return currmax


print(Solution.maxProfit(1, [7,3,5,1,6,4]))

# Success
# Details 
# Runtime: 1812 ms, faster than 19.98% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 24.9 MB, less than 95.39% of Python3 online submissions for Best Time to Buy and Sell Stock.