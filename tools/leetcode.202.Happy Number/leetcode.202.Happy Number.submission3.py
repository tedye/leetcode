class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        #attempt two - iterative
        while 1:
            n = sum([int(i)*int(i) for i in list(str(n))])
            if n == 1: return True
            if n == 4: return False
            