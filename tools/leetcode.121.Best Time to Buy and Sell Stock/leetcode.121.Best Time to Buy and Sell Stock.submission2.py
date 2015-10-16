class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        mi = prices[0]
        m = 0
        for i in range(1,len(prices)):
            if prices[i] >= mi:
                m = max(m, prices[i] - mi)
            else:
                mi = prices[i]
        return m
        