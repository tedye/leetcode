class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # sweep through the matrix
        m = len(board)
        if not m:
            return
        n = len(board[0])
        if not n:
            return
        
        for i in range(m):
            for j in range(n):
                count = 0
                for ii in range(max(i-1, 0), min(i+2, m)):
                    for jj in range(max(j-1, 0), min(j+2, n)):
                        count += board[ii][jj] & 1
                if (count == 4 and board[i][j]) or count == 3:
                    board[i][j] |= 16

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 4
        