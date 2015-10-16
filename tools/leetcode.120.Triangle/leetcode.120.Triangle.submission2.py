class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle: return 0
        if len(triangle) == 1: return triangle[0][0]
        
        res = triangle[-1][:]
        level = len(res)
        
        while level > 1:
            tempr = [0] * (level-1)
            temp = triangle[level-2]
            for i in range(level-1):
                tempr[level-2-i] = temp[level-2-i] + min(res[level-2-i],res[level-1-i])
            res = tempr
            level -= 1
        return res[0]
                
        
        