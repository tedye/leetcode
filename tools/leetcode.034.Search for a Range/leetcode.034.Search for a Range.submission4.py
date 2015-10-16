class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if not nums: return []
        res = []
        start = 0
        end = l = len(nums)
        found = None
        while start < end:
            mid = (start+end) // 2
            if nums[mid] == target:
                found = mid
                break
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid
        left = right = -1
        if found != None:
            left = right = mid
            while left > 0 and nums[left-1] == target:
                left -= 1
            while right < l-1 and nums[right+1] == target:
                right += 1
        return [left, right]

        