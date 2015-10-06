class Solution(object):
    def __init__(self):
        self.counter = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.counter = 0
        if n <= 0:
            return 0
        line = (1 << n) - 1
        self.helper(0,0,0,line)
        return self.counter
    
    def helper(self, col, left, right, line):
        if line == col:
            self.counter += 1
            return
        avail_pos = line & (~(col|left|right))
        while avail_pos:
            p = avail_pos & (~avail_pos+1)
            avail_pos -= p
            self.helper(col|p, (left|p) << 1, (right | p) >> 1, line)