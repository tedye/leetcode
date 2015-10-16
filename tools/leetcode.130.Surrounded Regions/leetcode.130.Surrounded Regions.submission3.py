class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board: return
        m = len(board)
        n = len(board[0])
        if n < 2 or m < 2: return
        
        pos = []
        for i in range(m):
            if board[i][0] == 'O':
                pos.append([i,0])
            if board[i][n-1] == 'O':
                pos.append([i,n-1])
        
        for j in range(n):
            if board[0][j] == 'O':
                pos.append([0,j])
            if board[m-1][j] == 'O':
                pos.append([m-1,j])

        c = 0
        while c < len(pos):
            i = pos[c][0]
            j = pos[c][1]
            board[i][j] = 'o'
            if i>0 and board[i-1][j] == 'O': pos.append([i-1,j])
            if i<m-1 and board[i+1][j] == 'O': pos.append([i+1,j])
            if j>0 and board[i][j-1] == 'O': pos.append([i,j-1])
            if j<n-1 and board[i][j+1] == 'O': pos.append([i,j+1])
            c += 1

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'o':
                    board[i][j] = 'O'
        