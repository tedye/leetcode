class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle: return 0
        if len(triangle) == 1: return triangle[0][0]
        
        n = len(triangle)
        res = [0] * len(triangle)
        
        self.helper(n,triangle,res)
        
        return min(res)
        
    def helper(self,n,triangle,res):
        if n == 1:
            res[0] = triangle[0][0]
            return
        self.helper(n-1,triangle,res)
        cur = triangle[n-1]
        temp = res[:]
        for i in range(n):
            if i == 0:
                res[i] = temp[i] + cur[i]
            elif i == n-1:
                res[i] = temp[i-1] + cur[i]
            else:
                res[i] = min(temp[i-1],temp[i]) + cur[i]
                
        