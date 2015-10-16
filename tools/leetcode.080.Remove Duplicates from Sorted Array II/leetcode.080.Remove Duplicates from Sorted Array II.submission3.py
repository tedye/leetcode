class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A: return 0
        if len(A) < 3 : return len(A)
        
        A.append(0x7fffffff)
        e = len(A) 
        cur = p = 0

        while p < e:
            if A[p] != A[cur]:
                x = max(0, p - cur - 2)
                if x > 0:
                    cnt = x
                    while cnt > 0:
                        del A[p - 1]
                        p -= 1
                        cnt -= 1
                        e -= 1
                cur = p
            p +=1
        del A[-1]
        e -= 1
        return e
            