class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        length = len(prices)
        ma = [0] * (length+1)
        mi = [0] * (length+1)
        ma[-1] = 0
        mi[0] = 0x7fffffff
        for i in range(length):
            ma[length-1-i] = max( ma[length-i], prices[length-1-i])
            mi[i+1] = min( mi[i], prices[i])
        m = 0
        for i in range(length):
            if ma[i+1] - mi[i+1] > m:
                m = ma[i+1] - mi[i+1]
        return m
            