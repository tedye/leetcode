class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if not nums or len(nums) == 1:
            return 0
        rightBound = nums[0]
        l = len(nums) 
        i = 0
        count = 1
        while i < l:
            if rightBound >= l-1:
                return count
            nrightBound = nums[i]
            while i < l and i <= rightBound:
                nrightBound = max(i+nums[i], nrightBound)
                i += 1
            if rightBound == nrightBound:
                break
            else:
                count += 1
                rightBound = nrightBound
        return -1
        