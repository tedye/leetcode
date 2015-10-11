class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # naive approach - brute force
        '''
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k] < target:
                        count += 1
        return count
        # fail to pass the large testing case as expected
        '''
        # sort first and then use three pointers
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        count = 0
        for i in range(1, n - 1):
            start = 0
            end = n - 1
            cur = target - nums[i]
            # search for valid tuple in O(n)
            while start < i and end > i:
                if nums[start] + nums[end] < cur:
                    count += end - i
                    start += 1
                else:
                    end -= 1
        return count
        
        