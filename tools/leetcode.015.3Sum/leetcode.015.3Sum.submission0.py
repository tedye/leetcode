class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        result = set()
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        for i in range(len(nums)):
            temp = nums[i]
            d[temp] -= 1
            r = set(nums[i+1:])
            for j in r:
                if -temp-j in r:
                    if -temp - j == j and d[j] > 1 or -temp-j != j:
                        result.add(tuple(sorted([temp,j,-temp-j])))
            d[temp] += 1
        return [list(i) for i in result]        