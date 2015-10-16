class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        lm = [0] * 3
        gm = [0] * 3
        
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            t = 2
            while t > 0:
                lm[t] = max(gm[t-1]+max(diff,0),lm[t]+diff)
                gm[t] = max(lm[t],gm[t])
                t -= 1
        return gm[-1]