class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        l = 0
        r = n - 1
        u = 0
        d = m - 1
        
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        count = 0
        
        res = []
        x = 0
        y = 0
        ox = -1
        oy = -1
        while l <= r or u <= d:
            if count == 4:
                count = 0
            if l <= x <= r and u <= y <= d:
                res.append(matrix[y][x])
                y += direction[count][0]
                x += direction[count][1]
            elif x > r:
                u += 1
                x -= 1
                y += 1
                count += 1
            elif y > d:
                r -= 1
                y -= 1
                x -= 1
                count += 1
            elif x < l:
                d -= 1
                x += 1
                y -= 1
                count += 1
            elif y < u:
                l += 1
                y += 1
                x += 1
                count +=1
        return res