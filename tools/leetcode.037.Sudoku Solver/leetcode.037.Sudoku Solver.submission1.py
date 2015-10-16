class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        hset = [{'1','2','3','4','5','6','7','8','9'} for _ in range(9)]
        vset = [{'1','2','3','4','5','6','7','8','9'} for _ in range(9)]
        boxset = [{'1','2','3','4','5','6','7','8','9'}for _ in range(9)]
        temp = self.solver(board,hset,vset,boxset)
        board[:] = temp[:]
        
    def solver(self, board, h, v, b):
        q = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    q.append([(i,j), h[i], v[j], b[(i//3) * 3 + j // 3]])
                else:
                    num = board[i][j]
                    h[i] -= {num}
                    v[j] -= {num}
                    b[(i//3) * 3 + j // 3] -= {num}
        while q:
            q.sort(key = lambda x: len(x[1] & x[2] & x[3]))
            cur = q.pop(0)
            avail = cur[1]&cur[2]&cur[3]
            i = cur[0][0]
            j = cur[0][1]
            if len(avail) == 0:
                return []
            elif len(avail) == 1:
                num = avail.pop()
                h[i] -= {num}
                v[j] -= {num}
                b[(i//3) * 3 + j // 3] -= {num}
                board[i][j] = num
            else:
                l = len(avail)
                for k in range(l):
                    num = avail.pop()
                    h[i] -= {num}
                    v[j] -= {num}
                    b[(i//3) * 3 + j // 3] -= {num}
                    board[i][j] = num
                    temp = self.solver([x[:] for x in board], [set(a) for a in h], [set(a) for a in v], [set(a) for a in b])
                    if temp:
                        return temp
                    board[i][j] = '.'
                    h[i].add(num)
                    v[j].add(num)
                    b[(i//3) * 3 + j // 3].add(num)
                return []
        return board
                
                
                
                