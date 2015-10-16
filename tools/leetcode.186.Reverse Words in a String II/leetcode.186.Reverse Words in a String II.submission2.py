class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        self.reverse(s, 0, len(s))
        
        i = 0
        for j in xrange(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                self.reverse(s, i, j)
                i = j + 1
    
    def reverse(self, s, begin, end):
        for i in xrange((end - begin) / 2):
            s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]