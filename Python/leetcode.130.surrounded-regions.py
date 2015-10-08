class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        
        q = set()
        for i in range(n):
            if board[0][i] == 'O':
                q.add((0,i))
            if board[m-1][i] == 'O':
                q.add((m-1,i))
        
        for j in range(m):
            if board[j][0] == 'O':
                q.add((j,0))
            if board[j][n-1] == 'O':
                q.add((j,n-1))
        
        while q:
            pos = q.pop()
            y = pos[0]
            x = pos[1]
            board[y][x] = '#'
            if x > 0 and board[y][x-1] == 'O': q.add((y,x-1))
            if y > 0 and board[y-1][x] == 'O': q.add((y-1,x))
            if x < n-1 and board[y][x+1] == 'O': q.add((y,x+1))
            if y < m-1 and board[y+1][x] == 'O': q.add((y+1,x))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'