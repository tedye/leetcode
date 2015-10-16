class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if not nums or k <= 0: 
            return False
        if len(nums) <= k+1:
            return len(set(nums)) != len(nums)
        size = 0
        workingset = set()
        for ind,i in enumerate(nums):
            if i in workingset:
                return True
            if size < k:
                workingset.add(i)
                size += 1
            else:
                workingset.remove(nums[ind - k])
                workingset.add(i)
        return False
        