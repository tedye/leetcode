class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2 : return 0
        if len(prices) == 2: return max(prices[1] - prices[0],0)
        
        left = [0] * len(prices)
        curMin = prices[0]
        MaxProfit = 0
        left[0] = MaxProfit
        for i in range(1,len(prices)):
            MaxProfit = max(prices[i] - curMin, MaxProfit)
            curMin = min(prices[i], curMin)
            left[i] = MaxProfit
            
        right = [0] * len(prices)
        curMax = prices[-1]
        MaxProfit = 0
        right[-1] = MaxProfit
        for i in range(2,len(prices)+1):
            MaxProfit = max(curMax - prices[-i], MaxProfit)
            curMax = max(prices[-i] , curMax)
            right[-i] = MaxProfit
        res = max([left[i] + right[i+1] for i in range(1,len(prices) - 1) ])
        return max(0,res,max(left))
        