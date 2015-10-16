class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        if not s: return 0
        
        result = 0
        cnt = 1
        for i in s[::-1]:
            result += (ord(i) - ord('A') + 1)*cnt
            cnt *= 26
        return result