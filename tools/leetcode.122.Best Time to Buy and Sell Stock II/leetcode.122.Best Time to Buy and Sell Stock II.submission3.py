class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2 : return 0
        
        res = 0
        
        for i in range(1,len(prices)):
            res += max(prices[i] - prices[i-1],0)

        return res
        