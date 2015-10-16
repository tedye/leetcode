class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board: return 
        if not board[0]: return
        if len(board) < 3: return
        
        self.helpCheck(board)
        
    def helpCheck(self,board):
        high = 0
        low = len(board)
        left = 0
        right = len(board[0])
        t = True
        if type(board[0]) == list:
            t = False
        o = 'o'
        x = 'x'
        diff = ord('x') - ord(board[0][0]) 
        if diff == 41 or diff == 32:
            o = 'O'
            x = 'X'
            
        s = '#'
        bad = []
        
        for i in range(right):
            if board[0][i] == o:
                bad.append((0,i))
                if t:
                    board[0] = board[0][:i] + s + board[0][i+1:]
                else:
                    board[0][i] = s
            if board[low-1][i] == o:
                bad.append((low-1,i))
                if t:
                    board[low-1] = board[low-1][:i] + s + board[low-1][i+1:]
                else:
                    board[low-1][i] = s
        for i in range(low):
            if board[i][0] == o:
                bad.append((i,0))
                if t:
                    board[i] =  s + board[i][1:]
                else:
                    board[i][0] = s
            if board[i][right-1] == o:
                bad.append((i,right-1))
                if t:
                    board[i] = board[i][:right-1] + s
                else:
                    board[i][right-1] = s
        while bad:
            pos = bad[-1]
            del bad[-1]
            if pos[0] - 1 >= high and board[pos[0] - 1][pos[1]] == o:
                a =(pos[0]-1,pos[1])
                bad.append(a)
                if t:
                    board[pos[0] - 1] = board[pos[0] - 1][:pos[1]] + s + board[pos[0] - 1][pos[1]+1:]
                else:
                    board[pos[0] - 1][pos[1]] = s
            if pos[0] + 1 < low and board[pos[0] + 1][pos[1]] == o:
                a =(pos[0]+1,pos[1])
                bad.append(a)
                if t:
                    board[pos[0] + 1] = board[pos[0] + 1][:pos[1]] + s + board[pos[0] - 1][pos[1]+1:]
                else:
                    board[pos[0] + 1][pos[1]] = s
            if pos[1] - 1 >= left and board[pos[0]][pos[1] - 1] == o:
                a =(pos[0],pos[1]-1)
                bad.append(a)
                if t:
                    board[pos[0]] = board[pos[0]][:pos[1]-1] + s + board[pos[0]][pos[1]:]
                else:
                    board[pos[0]][pos[1] - 1] = s
            if pos[1] + 1 < right and board[pos[0]][pos[1] + 1] == o:
                a =(pos[0],pos[1]+1)
                bad.append(a)
                if t:
                    board[pos[0]] = board[pos[0]][:pos[1]+1] + s + board[pos[0]][pos[1]+2:]
                else:
                    board[pos[0]][pos[1] + 1] = s
            
        for i in range(low):
            for j in range(right):
                if board[i][j] == o:
                    if t:
                        board[i] = board[i][:j] + x + board[i][j+1:] 
                    else:
                        board[i][j] = x
                if board[i][j] == s:
                    if t:
                        board[i] = board[i][:j] + o + board[i][j+1:] 
                    else:
                        board[i][j] = o
            
