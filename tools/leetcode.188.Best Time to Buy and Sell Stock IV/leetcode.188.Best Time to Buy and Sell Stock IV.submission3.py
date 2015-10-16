class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        if not prices: return 0
        res = 0
        if k > len(prices)-2:
            for i in range(1,len(prices)):
                res += max(prices[i] - prices[i-1],0)
            return res
        
        gm = [0] * (k+1)
        lm = [0] * (k+1)
        
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            j = k
            while j > 0:
                lm[j] = max(gm[j-1]+max(diff,0),lm[j]+diff)
                gm[j] = max(gm[j],lm[j])
                j -= 1
        return gm[k]
    