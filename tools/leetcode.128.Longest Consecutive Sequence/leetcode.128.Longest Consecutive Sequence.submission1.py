class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        result = 0
        hashtable = set(nums)
        while hashtable:
            i = hashtable.pop()
            cnt = 1
            temp = i
            while temp+1 in hashtable:
                cnt += 1
                temp += 1
                hashtable.remove(temp)
            temp = i
            while temp-1 in hashtable:
                cnt += 1
                temp -=1
                hashtable.remove(temp)
            result = max(result, cnt)
        return result
        