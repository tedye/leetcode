class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        if len(nums) == 1: return 0
        end = len(nums)
        temp = [-0x7fffffff-2] + nums + [-0x7fffffff-2]
        start = 1
        while start <= end:
            mid = (start+end)//2
            if temp[mid-1] < temp[mid] and temp[mid] > temp[mid+1]:
                return mid-1
            elif temp[mid-1] < temp[mid]:
                start = mid+1
            elif temp[mid] > temp[mid+1]:
                end = mid-1
            else:
                start += 1