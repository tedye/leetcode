class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix: return []
        u = 0
        o = len(matrix)
        l = 0
        r = len(matrix[0])
        res = []
        while u < o and l < r:
            i = u
            j = l
            if j == r: break
            while j < r:
                res.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            if i == o: break
            while i < o:
                res.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            if j == l-1:
                break
            while j >= l:
                print(matrix[i][j])
                res.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            if i == u: break
            while i > u:
                res.append(matrix[i][j])
                i -= 1
            u += 1
            o -= 1
            l += 1
            r -= 1
        return res
            
            
                