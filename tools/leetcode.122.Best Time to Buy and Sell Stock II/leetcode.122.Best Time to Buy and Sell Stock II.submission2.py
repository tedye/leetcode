class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        m = 0
        for i in range(len(prices)-1):
            m += max(0,prices[i+1]-prices[i])
        return m
        