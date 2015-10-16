class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        
        res = [0] * n
        res[0] = 1
        res[1] = 2
        pos = 2
        while pos < n:
            res[pos] = res[pos-1] + res[pos-2]
            pos+=1
        return res[-1]
            