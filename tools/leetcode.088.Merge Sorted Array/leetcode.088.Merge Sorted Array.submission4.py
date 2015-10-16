class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if n == 0: return
        if m == 0:
            for i in range(n):
                A[i] = B[i]
            return
        
        pos = n + m - 1
        pa = m - 1
        pb = n - 1
        
        while pa != -1 and pb != -1:
            if A[pa] >= B[pb]:
                A[pos] = A[pa]
                pos -= 1
                pa -= 1
            else:
                A[pos] = B[pb]
                pos -= 1
                pb -= 1
        if pa == -1:
            while pb!=-1:
                A[pos] = B[pb]
                pos -= 1
                pb -= 1

        