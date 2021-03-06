class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        running_min = prices[0]
        running_max = 0
        for p in prices:
            if p > running_min:
                running_max = max(p-running_min, running_max)
            running_min = min(running_min, p)
        return running_max