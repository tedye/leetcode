class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        #attempt two - iterative
        while 1:
            temp = 0
            while n >0:
                digit = n%10
                temp += digit * digit
                n //=10
            n = temp
            if n == 1: return True
            if n == 4: return False
            