class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        s = set()
        for i in range(1,10):
            s.add(chr(ord('0') + i))
        
        for i in range(9):
            temp1 = set(s)
            temp2 = set(s)
            temp3 = set(s)
            for j in range(9):
                # check horizontal
                if board[i][j] != '.' and board[i][j] in temp1:
                    temp1.remove(board[i][j])
                elif board[i][j] != '.':
                    return False
                # check vertical
                if board[j][i] != '.' and board[j][i] in temp2:
                    temp2.remove(board[j][i])
                elif board[j][i] != '.':
                    return False
                # check box
                if board[(i // 3) * 3 + j // 3 ][ (i % 3) * 3 + j % 3] != '.' and board[(i // 3) * 3 + j // 3 ][ (i % 3) * 3 + j % 3] in temp3:
                    temp3.remove(board[(i // 3) * 3 + j // 3 ][ (i % 3) * 3 + j % 3])
                elif board[(i // 3) * 3 + j // 3 ][ (i % 3) * 3 + j % 3] != '.':
                    return False
        return True