class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]