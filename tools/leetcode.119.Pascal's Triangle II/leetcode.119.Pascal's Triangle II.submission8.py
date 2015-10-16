class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        temp = []
        for i in range(0,rowIndex+1):
            temp.append(self.combination(rowIndex,i))
        return temp
        
    def combination(self,n,k):
        return self.factorials(n)/(self.factorials(n-k)*self.factorials(k))
    def factorials(self,n):
        if n == 0 or n == 1:
            return 1
            
        return n * self.factorials(n-1)