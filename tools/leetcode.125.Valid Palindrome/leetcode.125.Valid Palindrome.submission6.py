class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        # attempt two
        start = 0
        end = len(s) - 1
        while end > start:
            while end >= 0 and not s[end].isalnum():
                end -= 1
            while start < len(s) and not s[start].isalnum():
                start += 1

            if start != len(s) and end != 0 and s[start].lower() != s[end].lower():
                return False
            end -= 1
            start += 1
        return True