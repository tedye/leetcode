class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        profit = 0
        localmin = prices[0]
        for i in range(len(prices)):
            localmin = min(localmin,prices[i])
            profit = max(profit,prices[i] - localmin)
        return profit
            