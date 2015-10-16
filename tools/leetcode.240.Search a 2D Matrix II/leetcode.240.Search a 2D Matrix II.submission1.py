class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
            
        for i in range(len(matrix)):
            if self.bsearch(matrix[i],target):
                return True
        return False
    def bsearch(self, l, target):
        col = len(l)
        j = 0
        while j < col:
            mid = j + (col - j) // 2
            if l[mid] == target:
                return True
            elif l[mid] < target:
                j = mid + 1
            else:
                col = mid
        return False  