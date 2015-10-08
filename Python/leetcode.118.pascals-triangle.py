class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        prev = [[1]]
        j = 1
        while j < numRows: 
            p = prev[-1]
            prev.append([1] +  [p[i]+p[i+1] for i in range(len(p)-1)] + [1])
            j += 1
        return prev