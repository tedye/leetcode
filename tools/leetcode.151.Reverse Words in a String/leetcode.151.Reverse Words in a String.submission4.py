class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if not s: return s
        
        l = [x for x in s.split() if x]
        return ' '.join(l[::-1])
        