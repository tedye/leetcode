class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if not A:return [-1,-1]
        start = end = -1
        try:
            start = A.index(target)
            end = len(A) - A[::-1].index(target) -1 
        except ValueError:
            pass
        
        return[start,end]
        