class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if len(A) <= 1: return
        
        dic = {}
        dic[0]=0
        dic[1]=0
        dic[2]=0
        for a in A:
            dic[a]+=1
        cnt = 0
        for i in range(len(A)):
            if i < dic[0]:
                A[i] = 0
            elif i < dic[0] + dic[1]:
                A[i] = 1
            else:
                A[i] = 2