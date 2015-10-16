class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if not nums: -1
        if len(nums) == 1: return 0
        right = [0,1]
        count = 1
        while 1:
            bound = right[1]
            for i in range(right[0],bound):
                right[1] = max(right[1], i+nums[i]+1)
                if right[1] > len(nums)-1:
                        return count
            right[0] = bound
            if right[0] == right[1]:
                break
            count += 1
        return count
