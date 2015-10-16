class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i]= 1
            else:
                d[i] += 1
        res = set()
        for i in range(len(nums)):
            t = nums[i]
            temp = set(nums[i+1:])
            target = -t
            d[t] -= 1
            for j in temp:
                if target - j in temp:
                    if target -j == j and d[j] > 1 or target -j != j:
                        res.add(tuple(sorted([t, j, target- j ])))
            d[t] += 1
            
        return [list(r) for r in res]
        