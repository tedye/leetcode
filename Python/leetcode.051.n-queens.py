class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 0:
            return []
        line = (1 << n) - 1
        res = []
        board = ['.' * n for _ in range(n)]
        self.helper(0,0,0, board, res, 0, line)
        return res
    
    def setQ(self, p, row, board, symbol):
        i = 0
        while not (p&1):
            p >>= 1
            i += 1
        board[row] = board[row][:i] + symbol + board[row][i+1:]
        
    def helper(self, col, left, right, board, res, row, line):
        if line == col:
            res.append(board[:])
            return
        available_pos = (~(col|left|right)) & line
        while available_pos:
            new = (available_pos - 1) & available_pos
            p = available_pos - new
            available_pos = new
            self.setQ(p, row, board, 'Q')
            self.helper(col|p, (left|p) << 1, (right|p) >> 1, board, res, row+1, line)
            self.setQ(p, row, board, '.')