class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        # attempt two - bit manipulation
        # assume int length is 4 bytes
        bit_bucket = [0] * 32
        for element in nums:
            for i in range(32):
                if (element & (1 << i)):
                    bit_bucket[i]+=1
        res = 0
        length = len(nums) // 2
        for i in range(len(bit_bucket)-1):
            if bit_bucket[i] > length:
                res += 1 << i
        if bit_bucket[-1] > length:
            return -((res^0x7fffffff)+1)
        else:
            return res
            