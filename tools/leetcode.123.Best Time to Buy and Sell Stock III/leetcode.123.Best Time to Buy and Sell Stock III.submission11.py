class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2 : return 0
        if len(prices) == 2: return max(prices[1] - prices[0],0)
        
        left = [0] * len(prices)
        curMin = prices[0]
        MaxProfitl = 0
        left[0] = MaxProfitl
        
        right = [0] * len(prices)
        curMax = prices[-1]
        MaxProfitr = 0
        right[-1] = MaxProfitr
        
        for i in range(1,len(prices)):
            MaxProfitl = max(prices[i] - curMin, MaxProfitl)
            curMin = min(prices[i], curMin)
            left[i] = MaxProfitl
            MaxProfitr = max(curMax - prices[-i-1], MaxProfitr)
            curMax = max(prices[-i-1] , curMax)
            right[-i-1] = MaxProfitr

        res = max([left[i] + right[i+1] for i in range(1,len(prices) - 1) ])
        return max(0,res,max(left))
        