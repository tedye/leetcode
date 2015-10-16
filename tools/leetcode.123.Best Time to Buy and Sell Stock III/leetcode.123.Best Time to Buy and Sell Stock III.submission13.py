class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2 : return 0
        if len(prices) == 2: return max(prices[1] - prices[0],0)
        
        left = [0] * len(prices)
        self.maxProfitOne(prices,left)
        right = [0] * len(prices)
        self.maxProfitTwo(prices,right)
        res = 0
        for i in range(1,len(prices) - 1):
            res = max(res, left[i] + right[i+1])
        return max(res,max(left))

    def maxProfitOne(self, prices, res):
        curMin = prices[0]
        MaxProfit = 0
        res[0] = MaxProfit
        for i in range(1,len(prices)):
            MaxProfit = max(prices[i] - curMin, MaxProfit)
            curMin = min(prices[i], curMin)
            res[i] = MaxProfit

    def maxProfitTwo(self,prices,res):
        curMax = prices[-1]
        MaxProfit = 0
        res[-1] = MaxProfit
        for i in range(2,len(prices)+1):
            MaxProfit = max(curMax - prices[-i], MaxProfit)
            curMax = max(prices[-i] , curMax)
            res[-i] = MaxProfit
        