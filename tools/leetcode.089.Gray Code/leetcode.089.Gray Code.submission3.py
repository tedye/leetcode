class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        if n == 0: return [0]
        b = ['0','1']
        j = 1
        while j < n:
            b = ['0'+i for i in b]+['1'+i for i in b[::-1]]
            j += 1
        return [int(x, base=2) for x in b]
        