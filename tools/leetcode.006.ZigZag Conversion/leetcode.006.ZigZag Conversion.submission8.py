class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1: return s
        if nRows == 2: return s[::2]+s[1::2]
        
        res = [""] * nRows
        direction = True
        pos = 0
        for a in s:
            res[pos] += a
            if direction:
                pos += 1
                if pos == nRows - 1:
                    direction = False
            else:
                pos -= 1
                if pos == 0:
                    direction = True
        
        return "".join(res)
            