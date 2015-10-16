class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        visited = [False] * (m * n)
        for i in range(m):
            for j in range(n):
                if self.helper(board,visited,word,i,j,0,m,n):
                    return True
        return False

    def helper(self,board,visited,word,i,j,level,m,n):
        if level == len(word):
            return True
        elif i < 0 or i >= m or j < 0 or j >= n or visited[i*n+j] or word[level] != board[i][j]:
            return False
        else:
            visited[i*n+j] = True
            if self.helper(board,visited,word,i-1,j,level+1,m,n) \
                or self.helper(board,visited,word,i+1,j,level+1,m,n) \
                or self.helper(board,visited,word,i,j-1,level+1,m,n) \
                or self.helper(board,visited,word,i,j+1,level+1,m,n):
                return True
            visited[i*n+j] = False
            return False
        
            
            
        