class Solution:
    # @return an integer
    def maxArea(self, height):
        if not height:
            return 0
        result = 0
        i = 0
        j = len(height) - 1
        while i < j:
            result = max(result,(j - i) * min(height[i],height[j]))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return result