class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board: return False
        
        m = len(board)
        n = len(board[0])
        
        visited = [False] * m * n
        
        for i in range(m):
            for j in range(n):
                if self.helper(board,word,visited,i,j,0,m,n):
                    return True
        return False
        
    def helper(self,board,word,visited,i,j,level,m,n):
        if level == len(word):
            return True
        if i < 0 or i == m or j < 0 or j == n or visited[i*n+j] or board[i][j] != word[level]:
            return False
        visited[i*n+j] = True
        flag = False
        flag |= self.helper(board,word,visited,i+1,j,level+1,m,n)
        flag |= self.helper(board,word,visited,i-1,j,level+1,m,n)
        flag |= self.helper(board,word,visited,i,j+1,level+1,m,n)
        flag |= self.helper(board,word,visited,i,j-1,level+1,m,n)
        if flag:
            return True
        visited[i*n+j] = False
        return False