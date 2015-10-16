class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        # Horizontal
        for i in range(9):
            h = set()
            v = set()
            c = set()
            for j in range(9):
                if board[i][j] not in h:
                    h.add(board[i][j])
                elif board[i][j] != '.':
                    return False
                
                if board[j][i] not in v:
                    v.add(board[j][i])
                elif board[j][i] != '.':
                    return False
                
                if board[(i//3)*3+(j//3)][(i%3)*3+(j%3)] not in c:
                    c.add(board[(i//3)*3+(j//3)][(i%3)*3+(j%3)])
                elif board[(i//3)*3+(j//3)][(i%3)*3+(j%3)] != '.':
                    return False
        return True
        