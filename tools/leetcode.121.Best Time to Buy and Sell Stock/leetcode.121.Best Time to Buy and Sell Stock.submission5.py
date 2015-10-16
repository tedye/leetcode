class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        
        curMin = prices[0]
        MaxProfit = 0
        
        for i in range(1,len(prices)):
            if prices[i] - curMin > MaxProfit:
                MaxProfit = prices[i] - curMin
            if prices[i] < curMin:
                curMin = prices[i]
        
        return MaxProfit
            