class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        temp = x
        res = 0
        while temp > 0:
            res *= 10
            res += temp % 10
            temp //= 10
        return res == x
        