class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        #attempt one 
        if n == 1:
            return True
        elif n == 4: 
            return False
        else:
            next =sum([int(i)*int(i) for i in list(str(n))])
            return self.isHappy(next)
            
        