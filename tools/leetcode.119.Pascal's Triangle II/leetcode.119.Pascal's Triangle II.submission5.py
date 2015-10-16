class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        prev = [0] + self.getRow(rowIndex-1) + [0]
        return [prev[i]+prev[i+1] for i in range(len(prev)-1)]
        