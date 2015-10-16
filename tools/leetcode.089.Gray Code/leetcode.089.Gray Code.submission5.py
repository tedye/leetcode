class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        if n == 0: return [0]
        res = self.helper(n)
        return [int(i, base=2) for i in res]
        
    def helper(self,n):
        if n == 1:
            return ['0','1']
        r = self.helper(n-1)
        return ['0'+i for i in r]+['1'+i for i in r[::-1]]
        