class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        import functools
        if not nums:
            return ''
        
        res= ''.join(sorted([str(x) for x in nums], key = functools.cmp_to_key(self.compare))).lstrip('0')
        if not res:
            return '0'
        else:
            return res
    
    
    def compare(self,x,y):
        a = int(x+y)
        b = int(y+x)
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1