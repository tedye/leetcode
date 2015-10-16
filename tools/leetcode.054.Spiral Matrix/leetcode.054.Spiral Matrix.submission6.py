class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0: return []

        l = 0
        lb = 0
        r = len(matrix[0])
        
        u = 0
        ub = 0
        d = len(matrix)
        
        res = []
        while 1:
            if l == r-lb:
                break
            while l < r-lb:
                res.append(matrix[u][l])
                l+=1
            u += 1
            l -= 1
            
            if u == d-ub:
                break
            while u < d-ub:
                res.append(matrix[u][l])
                u += 1
            u -= 1
            l -= 1
            
            if l < lb:
                break
            
            while l >= lb:
                res.append(matrix[u][l])
                l -= 1
            l += 1
            u -= 1
            
            if u <= ub:
                break
            while u > ub:
                res.append(matrix[u][l])
                u -= 1
            u += 1
            l += 1
            lb += 1
            ub += 1
        return res
            
        