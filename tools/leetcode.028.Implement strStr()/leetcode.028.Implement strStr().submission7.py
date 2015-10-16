class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle): return -1
        if needle == haystack: return 0
        if needle == "": return 0
        
        # allow indexing into pattern and protect against change during yield
        pattern = list(needle)
     
        # build table of shift amounts
        shifts = [1] * (len(pattern) + 1)
        shift = 1
        for pos in range(len(pattern)):
            while shift <= pos and pattern[pos] != pattern[pos-shift]:
                shift += shifts[pos-shift]
            shifts[pos+1] = shift
     
        # do the actual search
        startPos = 0
        matchLen = 0
        for c in haystack:
            while matchLen == len(pattern) or \
                  matchLen >= 0 and pattern[matchLen] != c:
                startPos += shifts[matchLen]
                matchLen -= shifts[matchLen]
            matchLen += 1
            if matchLen == len(pattern):
                return startPos
        return -1