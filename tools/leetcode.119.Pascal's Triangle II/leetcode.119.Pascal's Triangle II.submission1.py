class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        rowIndex += 1
        if rowIndex <= 0:
            return []
        
        cur = [1]
        j = 1
        while j < rowIndex:
            cur = [1] + [cur[i]+cur[i+1] for i in range(len(cur)-1)] + [1]
            j += 1
        return cur