class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0: return 0
        val = x * 0.5 + 0.5
        last = 0
        eps = 0.5
        while 1:
            last = val
            val = (val+x/val) * 0.5
            if abs(val-last) < eps:
                break
        return int(val)
            
        