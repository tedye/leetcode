class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        i = 0
        l = len(nums) - 1
        while i < l:
            if nums[i] < nums[l]:
                return nums[i]
            mid = i + (l-i) // 2
            if nums[mid] > nums[i]:
                i = mid + 1
            elif nums[mid] < nums[i]:
                l = mid
            else:
                i += 1
        return min(nums[i], nums[l])