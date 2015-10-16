class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1: return s
        if nRows == 2: return s[::2] + s[1::2]
        
        mod = nRows * 2 - 2
        res = ''
        for i in range(nRows):

            if i == 0 or i == nRows - 1:
                res += s[i::mod]
            else:
                a = s[i::mod]
                b = s[mod-i::mod]
                c = ''
                for i in range(len(a)):
                    if i !=  len(b):
                        c += a[i]+b[i]
                    else:
                        c += a[i]
                res += c
        return res
                