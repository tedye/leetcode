class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        i = 0
        length = len(A)
        while i < length:
            while A[i] != i+1 and 1<= A[i] <= length and A[A[i]-1] != A[i]:
                temp = A[i]
                A[i] = A[A[i]-1]
                A[temp-1] = temp
            i += 1
        for i in range(len(A)):
            if A[i] != i+1:
                return i+1
        return length+1
        