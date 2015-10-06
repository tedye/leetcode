class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        l = 0
        r = n-1
        u = 0
        d = n-1
        while l <= r:
            for i in range(r-l):
                [matrix[u][l+i],matrix[u+i][r],matrix[d][r-i],matrix[d-i][l]] = [matrix[d-i][l],matrix[u][l+i],matrix[u+i][r],matrix[d][r-i]] 
            l += 1
            r -= 1
            u += 1
            d -= 1