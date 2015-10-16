class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        mask = 1
        i = 0
        while i < 32:
            if n & mask:
                count += 1
            mask <<= 1
            i += 1
            
        return count
        
        
        