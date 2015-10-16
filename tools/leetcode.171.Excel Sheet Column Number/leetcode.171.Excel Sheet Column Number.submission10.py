class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        if not s: return 0
        
        result = 0
        b = list(s)
        cnt = 1
        for i in b[::-1]:
            
            result += (ord(i) - ord('A') + 1)*cnt
            cnt *= 26
        return result