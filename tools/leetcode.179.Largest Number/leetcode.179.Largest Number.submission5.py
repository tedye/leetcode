class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums: return ''
        if len(nums) == 1: return str(nums[0])
        import functools
        res = ''.join(sorted([str(x) for x in nums],key=functools.cmp_to_key(self.compare),reverse=True)).lstrip('0')
        if not res:
            return '0'
        return res

    def compare(self, x, y):
        left = int(y+x)
        right = int(x+y)
        if right > left:
            return 1
        elif right < left:
            return -1
        else:
            return 0
        