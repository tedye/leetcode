class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        res = [""] * numRows
        length = 2*numRows-2
        for i in range(len(s)):
            row = i%length
            if row < numRows:
                res[row]+=s[i]
            else:
                res[length - row] += s[i]
                
        return ''.join(res)
        