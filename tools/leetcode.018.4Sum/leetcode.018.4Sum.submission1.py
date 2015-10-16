class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                t = target -nums[i] - nums[j]
                s = j + 1
                e = len(nums) - 1
                while s < e:
                    x = nums[s] +  nums[e]
                    if x == t:
                        res.add(tuple([nums[i],nums[j], nums[s], nums[e]]))
                    if x < t:
                        s += 1
                    else:
                        e -= 1
        return [list(r) for r in res]
                