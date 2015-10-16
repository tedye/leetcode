class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        l = len(prices)
        if l < 2: return 0
        if l == 2:
            return max(0,prices[1]-prices[0])
        left = [0] * l
        right = [0] * l
        curMax = prices[-1]
        curMin = prices[0]
        
        for i in range(l-1):
            if prices[i] < prices[i+1]:
                left[i+1] = max(left[i],prices[i+1] - curMin)
            else:
                curMin = min(curMin,prices[i+1])
                left[i+1] = left[i]
            if prices[l-i-1] > prices[l-i-2]:
                right[l-i-2] = min(right[l-i-1], prices[l-i-2]-curMax)
            else:
                curMax = max(curMax,prices[l-i-2])
                right[l-i-2] = right[l-i-1]
        m = left[-1]
        for i in range(l-1):
            m = max(m, left[i]-right[i+1])
        return m
        
        