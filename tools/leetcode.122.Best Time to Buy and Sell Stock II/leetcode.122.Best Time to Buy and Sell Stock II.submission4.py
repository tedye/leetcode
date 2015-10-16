class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2 : return 0
        
        curMin = curMax = prices[0]
        MaxProfit = localProfit = 0
        
        for i in range(1,len(prices)):
            p = prices[i]
            if p < curMax or i == len(prices) - 1:
                if p > curMax:
                    localProfit = max(localProfit, p - curMin)
                MaxProfit += localProfit
                curMin = curMax = p
                localProfit = 0
            
            curMin = min(curMin,p)
            curMax = max(curMax,p)
            localProfit = max(localProfit, p - curMin)

        return MaxProfit