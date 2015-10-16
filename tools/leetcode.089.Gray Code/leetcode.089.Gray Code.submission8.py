class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0: return [0]
        a = 1 << (n-1)
        temp = self.grayCode(n-1)
        return temp +[ t + a for t in temp[::-1]]
        