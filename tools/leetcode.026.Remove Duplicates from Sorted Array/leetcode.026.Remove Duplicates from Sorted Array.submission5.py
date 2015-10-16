class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:return 0
        if len(A) == 1:return 1
        
        cnt1 = 0
        cnt2 = 1
        while cnt2 != len(A):
            if A[cnt1] == A[cnt2]:
                cnt2 += 1
            else: 
                A[cnt1 + 1] = A[cnt2]
                cnt1 += 1
                cnt2 += 1
        A = A[:cnt1 + 1]
        return cnt1 + 1