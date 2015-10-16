class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if not s:
            return s
            
        A = s + s[::-1]
        prefix = self.getPrefix(A)
            
        return s[prefix[-1]+1:][::-1] + s
        
    def getPrefix(self, pattern):
        prefix = [-1] * len(pattern)
        j = -1
        for i in xrange(1, len(pattern)):
            while j > -1 and pattern[j+1] != pattern[i]:
                j = prefix[j]
            if pattern[j+1] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix
        