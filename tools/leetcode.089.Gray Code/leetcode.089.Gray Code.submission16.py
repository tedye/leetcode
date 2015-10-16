class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
        temp = self.grayCode(n-1)
        temp1 = [2**(n-1) + i for i in temp[::-1]]
        return temp + temp1
