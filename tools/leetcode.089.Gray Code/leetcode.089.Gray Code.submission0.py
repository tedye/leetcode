class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return [0]
        i = 1
        res = ['0','1']
        while i < n:
            res = ['0'+j for j in res] + ['1'+j for j in res[::-1]]
            i += 1
        return [int(k,base=2) for k in res]