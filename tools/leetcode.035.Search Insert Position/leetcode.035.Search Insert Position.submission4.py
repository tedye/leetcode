class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if not A: return 0
        if target < A[0]: return 0
        if target > A[-1]: return len(A)
        temp = 0x7fffffff
        for i in range(len(A)):
            if A[i] == target:
                return i
            if temp < target and A[i] > target:
                return i
            temp = A[i]
