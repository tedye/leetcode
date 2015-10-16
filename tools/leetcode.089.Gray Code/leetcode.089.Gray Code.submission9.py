class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0: return [0]
        if n == 1: return [0,1]
        if n == 2: return [0,1,3,2]
        temp = self.grayCode(n-1)
        return temp +[ t + 2**(n-1) for t in temp[::-1]]
        