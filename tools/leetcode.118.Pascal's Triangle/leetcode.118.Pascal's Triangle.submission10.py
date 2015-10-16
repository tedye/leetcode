class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        temp = []
        if numRows <= 0:
            return []
        for i in range(numRows):
            temp.append(self.layermaker(i))
        return temp
    def layermaker(self,n):
        a = []
        for i in range(0,n+1):
            a.append(self.combination(n,i))
        return a
    def combination(self,n,k):
        return self.factorials(n) // ( self.factorials(n-k) * self.factorials(k))
    def factorials(self, n):
        if n <= 0 or n == 1: return 1
        return n * self.factorials(n - 1)