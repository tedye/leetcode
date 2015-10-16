class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        if len(height) < 3: return 0
        
        l = 0
        r = len(height)-1
        lM = height[l]
        rM = height[r]
        res = 0
        while l < r:
            if lM < rM:
                l += 1
                if height[l] < lM:
                    res += lM - height[l]
                else:
                    lM = height[l]
            else:
                r -= 1
                if height[r] < rM:
                    res += rM - height[r]
                else:
                    rM = height[r]
        return res
        