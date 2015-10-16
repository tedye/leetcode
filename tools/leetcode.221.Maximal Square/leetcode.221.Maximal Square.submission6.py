class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        for i in range(m):
            line = [0] * n
            for j in range(n):
                c = i
                while c >= 0 and matrix[c][j] == '1':
                    line[j] += 1
                    c -= 1
            res = max(res,self.getArea(line))
        return res
        
    def getArea(self,line):
        i = 0
        line.append(0)
        l = len(line)
        stack = []
        res = 0
        while i < l:
            if not stack or line[i] > line[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                H = line[stack.pop(-1)]
                if not stack:
                    res = max(res,min(H*H, i*i))
                else:
                    res = max(res, min( H*H, (i - stack[-1] - 1) * (i - stack[-1] - 1)))
        return res        