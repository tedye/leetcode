class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        if not s:
            return True
        
        start = 0
        end = len(s)-1
        s = s.lower()
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
            
        return True