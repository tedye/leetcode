class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join([x for x in s.split()[::-1]])
        
        