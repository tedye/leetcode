class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        t = str(x)
        return t[::-1]  == t