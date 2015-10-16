class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        temp = self.helper(board)
        board[:] = temp[:]

    def helper(self,board):
        hset = [{'1','2','3','4','5','6','7','8','9'} for _ in range(9)]
        vset = [{'1','2','3','4','5','6','7','8','9'} for _ in range(9)]
        boxset = [{'1','2','3','4','5','6','7','8','9'}for _ in range(9)]
        
        working = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    working.append([(i,j),hset[i],vset[j],boxset[(i//3) * 3 + j // 3]])
                else:
                    hset[i] -= {board[i][j]}
                    vset[j] -= {board[i][j]}
                    boxset[(i//3) * 3 + j // 3] -= {board[i][j]}

        while working:
            working.sort(key=lambda x: len(x[1]&x[2]&x[3]))
            cur = working.pop(0)
            candi = (cur[1]&cur[2]&cur[3])
            if len(candi) == 0: return []
            if len(candi) == 1:
                num = candi.pop()
                i = cur[0][0]
                j = cur[0][1]
                hset[i] -= {num}
                vset[j] -= {num}
                boxset[(i//3) * 3 + j // 3] -= {num}
                board[i][j] = num
            else:
                l = len(candi)
                for k in range(l):
                    num = candi.pop()
                    i = cur[0][0]
                    j = cur[0][1]
                    board[i][j] = num
                    temp = self.helper([k[:] for k in board])
                    if temp:
                        board = temp
                        return board
                    board[i][j] = '.'
                return []
        return board
        