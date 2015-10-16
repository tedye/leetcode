class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n == 0: return []
        if n == 1: return [[1]]
        
        mat = [[0 for _ in range(n)] for _ in range(n)]
        u = l = 0
        o = r = n
        x = 1
        while u < o and l < r:
            i = u
            j = l
            
            if j == r: break
            while j < r:
                mat[i][j] = x
                x+= 1
                j+= 1
            j -= 1
            i += 1
            if i == o: break
            while i < o:
                mat[i][j] = x
                x+= 1
                i+= 1
            i -= 1
            j -= 1
            if j == l - 1: break
            while j >= l:
                mat[i][j] = x
                x+= 1
                j-= 1
            j += 1
            i -= 1
            if i == u: break
            while i > u:
                mat[i][j] = x
                x+= 1
                i-= 1
            u += 1
            l += 1
            o -= 1
            r -= 1
        return mat
                
                