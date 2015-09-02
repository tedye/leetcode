class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = [''] * numRows
        ind = 0
        direction = 1
        for i in range(len(s)):
            result[ind] += s[i]
            ind += direction
            if ind == -1:
                direction = 1
                ind = 1
            if ind == numRows:
                direction = -1
                ind = numRows - 2
        return ''.join(result)

