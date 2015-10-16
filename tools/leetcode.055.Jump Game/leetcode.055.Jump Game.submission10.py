class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if not A: return False
        if len(A) == 1: return True
        pos = 0
        l = len(A) - 2
        visited = set()
        maxCover = A[0]
        pos = 0
        while pos <= l and pos <= maxCover:
            cover = pos + A[pos]
            if cover > l:
                return True
            if cover > maxCover:
                maxCover = cover
            pos += 1

        return False
        