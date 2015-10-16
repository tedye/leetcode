class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        res = set()
        keys = {}
        for i in nums:
            if i not in keys:
                keys[i] = 1
            else:
                keys[i] += 1
        
        for i in keys:
            keys[i] -= 1
            for j in keys:
                if keys[j] == 0:
                    continue
                else:
                    keys[j] -= 1
                if (-i-j) in keys and keys[-i-j] > 0:
                    res.add(tuple(sorted([i,j,-i-j])))
                keys[j] += 1
            keys[i] += 1
        
        return list(res)
         