class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows <= 0:
            return []
        prev = [[1]]
        j = 1
        while j < numRows: 
            p = prev[-1]
            prev.append([1] +  [p[i]+p[i+1] for i in range(len(p)-1)] + [1])
            j += 1
        return prev
        