class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            testH = [0] * 9
            testV = [0] * 9
            testB = [0] * 9
            for j in range(9):
                if board[i][j] != '.':
                    #check row
                    testH[ord(board[i][j])-ord('1')] += 1
                if board[j][i] != '.':
                    #check col
                    testV[ord(board[j][i])-ord('1')] += 1
                if board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3] != '.':
                    #check box
                    testB[ord(board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]) - ord('1')] += 1
                    
            
            if max(testH) > 1 or max(testV) > 1 or max(testB) > 1:
                return False
        
        return True
    