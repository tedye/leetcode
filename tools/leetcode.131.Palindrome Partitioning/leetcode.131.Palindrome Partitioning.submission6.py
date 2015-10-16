class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s: return []
        if len(s) == 1: return [[s]]
        result = []
        current = []
        self.helper(s,current,result)
        return result
    
    def helper(self,s,current,result):
        if not s:
            result.append(current[:])
            return
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                current.append(s[:i+1])
                self.helper(s[i+1:],current,result)
                current.pop(-1)
                