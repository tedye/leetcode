class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        if n == 1:
            return [[1]]
        matrix = [[None] * n for _ in range(n)]
        x = y = 0
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        count = 1
        l = 0
        r = n-1
        u = 0
        d = n-1
        dc = 0
        while l <= r or u <= d:
            if l <= x <= r and u <= y <= d:
                matrix[y][x] = count
                count += 1
                y += direction[dc&3][0]
                x += direction[dc&3][1]
            elif x > r:
                u += 1
                x -= 1
                y += 1
                dc += 1
            elif y > d:
                r -= 1
                y -= 1
                x -= 1
                dc +=1
            elif x < l:
                d -= 1
                x += 1
                y -= 1
                dc += 1
            elif y < u:
                l += 1
                y += 1
                x += 1
                dc += 1
        return matrix