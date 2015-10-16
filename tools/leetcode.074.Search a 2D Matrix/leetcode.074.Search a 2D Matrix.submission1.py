class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0 
        l = m
        while i+1 < l:
            mid = i + (l-i) // 2
            print(mid)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                l = mid
            else:
                i = mid
        j = 0
        l = n - 1
        while j <= l:
            mid = j + (l-j) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                l = mid - 1
            else:
                j = mid + 1
        return False