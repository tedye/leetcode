class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # it is the same to find a path from top to bottom
        # can be solved by dynamic programming
        if not costs:
            return 0
        values = costs[0][:]
        for i in range(1, len(costs)):
            values = [costs[i][0] + min(values[1], values[2]), costs[i][1] + min(values[0], values[2]), costs[i][2] + min(values[0], values[1])]
        
        return min(values)
        