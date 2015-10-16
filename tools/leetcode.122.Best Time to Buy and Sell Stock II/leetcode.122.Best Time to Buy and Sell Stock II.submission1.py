class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        running_max = 0
        for i in range(1,len(prices)):
            running_max += max(0, prices[i] - prices[i-1])
        return running_max
        