class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l = 0
        r = len(num)
        while l < r:
            if r-l < 3: 
                return min(num) 
            mid = (l+r) // 2
            
            if num[l] < num[mid]:
                l = mid + 1
            elif num[l] > num[mid]:
                r = mid
            else:
                l += 1
            