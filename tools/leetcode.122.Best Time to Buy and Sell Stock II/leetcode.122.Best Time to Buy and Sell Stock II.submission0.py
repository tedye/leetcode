class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        running_max = 0
        for i in range(1,len(prices)):
            running_max += max(0, prices[i] - prices[i-1])
        return running_max
        