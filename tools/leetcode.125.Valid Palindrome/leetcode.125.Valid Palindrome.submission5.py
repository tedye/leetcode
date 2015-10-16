class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        # attempt three
        clean_s = [i.lower() for i in s if i.isalnum()]
        return clean_s == clean_s[::-1]