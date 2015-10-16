class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 or n == 1: return 1
        
        p = self.factorial(m+n-2)/(self.factorial(m-1)*self.factorial(n-1))
        return p

    def factorial(self,m):
        if m == 1: return 1
        return m * self.factorial(m - 1)
        