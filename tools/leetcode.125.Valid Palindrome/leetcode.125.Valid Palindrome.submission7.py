class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        clean_s = [i for i in list(s) if i.isalnum()]
        if len(clean_s) < 2:
            return True
        start = 0
        end = len(clean_s) -1 
        while end >= start:
            if clean_s[start].lower() != clean_s[end].lower():
                return False
            start += 1
            end -= 1
        return True
        