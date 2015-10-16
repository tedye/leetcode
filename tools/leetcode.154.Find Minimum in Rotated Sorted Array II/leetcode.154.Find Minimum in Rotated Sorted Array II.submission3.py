class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        i = 0
        l = len(num)-1
        
        while i < l:
            if num[i] < num[l]:
                return num[i]
            mid = i + (l-i) // 2
            if num[i] < num[mid]:
                i = mid + 1
            elif num[i] > num[mid]:
                l = mid
            else:
                i += 1
        return min(num[i],num[l])
                