class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # naive approach O(N^2)
        '''
        for n in nums:
            if nums.count(n) > 1:
                return n
        # failed to pass large testing cases (TLE)
        '''
        
        # O(nlgn)
        start = 1
        end = len(nums)-1
        while start < end:
            upperCount = 0
            lowerCount = 0
            mid = start + (end-start) // 2
            for n in nums:
                if end>= n > mid:
                    upperCount += 1
                elif start <= n <= mid:
                    lowerCount += 1
            if upperCount > end - mid:
                # duplicate in range mid + 1 to end
                start = mid+1
            else:
                end = mid
        return start