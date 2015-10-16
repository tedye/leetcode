class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n < 0:
            return 1.0/self.helper(x,-n)
        else:
            return self.helper(x,n)
        
    def helper(self,x,n):
        if n == 0:
            return 1
        
        t = self.helper(x, n//2)
        if n & 1:
            return t*t*x
        else:
            return t*t
            