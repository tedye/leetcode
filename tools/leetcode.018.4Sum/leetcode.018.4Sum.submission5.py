class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums) < 4: return []
        nums.sort()
        length = len(nums)
        res = set()
        for i in range(length-3):
            for j in range(i+1,length-2):
                tempTarget = target - nums[i] - nums[j]
                start = j+1
                end = length-1
                while start < end:
                    s = nums[start]+nums[end]
                    if s == tempTarget:
                        res.add((nums[i],nums[j],nums[start],nums[end]))
                        start += 1
                    elif s < tempTarget:
                        start += 1
                    else:
                        end -= 1
        return [list(i) for i in res]
                        