class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if not A: return None
        if len(A) == 1: return 0
        if A[0] > len(A)-2: return 1
        pos = 0
        l = len(A) - 2
        maxCover = A[0]
        pos = 0
        boundary = A[0]
        cnt = 1
        stop = False
        while not stop and pos <= maxCover:
            cover = pos + A[pos]
            if cover > l:
                cnt += 1
                stop = True
                continue
            if cover > maxCover:
                maxCover = cover
            if pos == boundary:
                cnt += 1
                boundary = maxCover 
            pos += 1
        if stop:
            return cnt
        else:
            return 0
            