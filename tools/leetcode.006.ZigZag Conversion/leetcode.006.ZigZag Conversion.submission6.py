class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1: return s
        if nRows == 2: return s[::2]+s[1::2]
        
        res = [""] * nRows
        mod = nRows * 2 - 2
        pos = [i for i in range(nRows)] + [-i for i in range(2,nRows)]
        for i in range(len(s)):
            res[pos[i % mod]] += s[i]
        
        return "".join(res)
            