class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0: return False
        
        d = {}
        for i in range(len(nums)):
            x = nums[i] / (t+1)
            if x in d or (x-1) in d and nums[i] - d[x-1] <= t or (x+1) in d and d[x+1] - nums[i] <= t:
                return True
            if len(d) >= k:
                last = nums[i-k] / (t+1)
                del d[last]
            d[x] = nums[i]
        return False
        