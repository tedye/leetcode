class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        l = len(nums)
        if l == 0: return 0
        if l < 3: return min(nums)
        
        start = 0
        end = l-1
        while start < end:
            if end - start < 4:
                return min(nums[start:end+1])
            mid = (start+end)//2
            if nums[mid] > nums[start] and nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[start] and nums[mid] < nums[end]:
                end = mid
            elif nums[start] < nums[mid] < nums[end]:
                return nums[start]
                