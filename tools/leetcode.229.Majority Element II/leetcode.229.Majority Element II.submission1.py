class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        l = len(nums) // 3
        d = {}
        result = set()
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
            if d[n] > l:
                result.add(n)
        return list(result)
        