class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        res = [[1]]
        cnt = 1
        while cnt < numRows:
            cur = [0]+res[-1]+[0]
            res.append([cur[i]+cur[i+1] for i in range(len(cur)-1)])
            cnt += 1
        return res
        