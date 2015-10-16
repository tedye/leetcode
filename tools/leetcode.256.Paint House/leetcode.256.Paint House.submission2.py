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
            oldvalues = values[:]
            values[0] = costs[i][0] + min(oldvalues[1], oldvalues[2])
            values[1] = costs[i][1] + min(oldvalues[0], oldvalues[2])
            values[2] = costs[i][2] + min(oldvalues[0], oldvalues[1])
        
        return min(values)
        