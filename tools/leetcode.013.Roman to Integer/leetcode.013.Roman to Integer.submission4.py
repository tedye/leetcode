class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        prev = ''
        res = 0
        for i in s:
            if i == 'M':
                if prev == 'C':
                    res += 800
                else:
                    res += 1000
            elif i == 'D':
                if prev == 'C':
                    res += 300
                else:
                    res += 500
            elif i == 'C':
                if prev == 'X':
                    res += 80
                else:
                    res += 100
            elif i == 'L':
                if prev == 'X':
                    res += 30
                else:
                    res += 50
            elif i == 'X':
                if prev == 'I':
                    res += 8
                else:
                    res += 10
            elif i == 'V':
                if prev == 'I':
                    res += 3
                else:
                    res += 5
            elif i == 'I':
                res += 1
            prev = i
        return res
        