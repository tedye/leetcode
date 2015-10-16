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
        
        for i in xrange(m):
            for j in xrange(n):
                count = 0
                for ii in xrange(max(i-1, 0), min(i+2, m)):
                    for jj in xrange(max(j-1, 0), min(j+2, n)):
                        count += board[ii][jj] & 1
                if (count == 4 and board[i][j]) or count == 3:
                    board[i][j] |= 16

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 4
        