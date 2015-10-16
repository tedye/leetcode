class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        
        left = 0
        right = len(height) - 1
        m = 0
        curLH = height[left]
        curRH = height[right]
        while left < right:
            if curLH < curRH:
                left += 1
                if height[left] < curLH:
                    m += curLH - height[left]
                else:
                    curLH = height[left]
            else:
                right -= 1
                if height[right] < curRH:
                    m += curRH - height[right]
                else:
                    curRH = height[right]
        return m