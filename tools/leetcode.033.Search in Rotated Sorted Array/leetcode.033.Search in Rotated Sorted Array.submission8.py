class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A) == 0 : return -1
        if len(A) == 1 : 
            if target == A[0]: 
                return 0
            else:
                return -1
        
        return self.helper(0,len(A)-1,A,target)
    
    def helper(self, start, end, A, target):
        if start >= end:
            if A[start] == target:
                return start
            else: return -1
        
        mid = (end-start) // 2 + start
        
        if A[start] < A[end]:
            print(start,end)
            # not rotated
            if target < A[start] or target > A[end]:
                return -1

            if A[mid] == target:
                return mid
            else:
                return max(self.helper(start,mid-1,A,target),self.helper(mid+1,end,A,target))
        else:
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                if A[mid] > A[start]:
                    return max(self.helper(start,mid-1,A,target),self.helper(mid+1,end,A,target))
                else:
                    if mid == start:
                        if A[end] == target:
                            return end 
                        else: 
                            return -1
                    else:
                        return self.helper(start,mid-1,A,target)
            else:
                if A[mid] > A[start]:
                    return self.helper(mid+1,end,A,target)
                else:
                    return max(self.helper(start,mid-1,A,target),self.helper(mid+1,end,A,target))
            
    