class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        if len(A) < 3:
            if target in A:
                return True
            else:
                return False
        l = 0
        r = len(A) - 1
        while l <= r:

            mid = (r+l) // 2
            
            if A[mid] == target:
                return True
            if A[mid] > A[l]:
                if A[l] <= target and A[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            elif A[mid] < A[l]:
                if A[l] <= target or A[mid] > target:
                    r = mid - 1
                else: 
                    l = mid + 1
            else:
                l +=1
        return False
        