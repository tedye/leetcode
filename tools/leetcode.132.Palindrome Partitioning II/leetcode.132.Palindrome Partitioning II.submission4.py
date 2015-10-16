class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if not s: return 0
        length = len(s)
        c = [length - i for i in range(length)] + [0]
        p = [[False] * length for _ in range(length)]
        start = length - 1
        while start >= 0:
            end = start
            while end < length:
                if s[end] == s[start] and (end - start < 2 or p[start+1][end-1]):
                    p[start][end] = True
                    c[start] = min(c[start],c[end+1]+1)
                end += 1
            start -= 1
        return c[0] - 1
        