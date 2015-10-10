class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        if k >= len(prices) - 1:
            m = 0
            for i in range(len(prices)-1):
                m += max(prices[i+1] - prices[i], 0)
            return m
        
        lm = [0] * (k+1)
        gm = [0] * (k+1)
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            t = k
            while t > 0:
                lm[t] = max(gm[t-1]+max(diff,0), lm[t] + diff)
                gm[t] = max(gm[t], lm[t])
                t -= 1
        return gm[-1]