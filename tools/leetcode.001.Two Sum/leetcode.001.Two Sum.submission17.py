class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        a = dict()
        for i,n in enumerate(num):
            if target - n in a:
                return (a[target-n],i+1)
            if n not in a:
                a[n] = i+1
        return None
