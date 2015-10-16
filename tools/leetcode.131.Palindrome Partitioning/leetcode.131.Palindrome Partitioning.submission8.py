class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s: return [[]]
        res = []
        for i in range(len(s)):
            if self.isP(s[:i+1]):
                print(s[:i+1])
                res += [[s[:i+1]] + e for e in  self.partition(s[i+1:])]
        return res
    
    def isP(self,s):
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
            
                