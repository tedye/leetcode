class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        l = len(nums) // 3
        result = []
        for i in set(nums):
            if nums.count(i) > l:
                result.append(i)
        return result
        
        
        