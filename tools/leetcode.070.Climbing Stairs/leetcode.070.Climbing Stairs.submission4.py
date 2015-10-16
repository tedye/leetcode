class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        options = n // 2
        sum = 0
        for i in range(options+1):
            sum += self.combinationfunc(i,n-i)
        return sum
    def combinationfunc(self,i,k):
        return self.factorials(k) / (self.factorials(i) * self.factorials(k - i))
    def factorials(self,x):
        if x == 1 or x == 0: return 1
        return x * self.factorials(x - 1)