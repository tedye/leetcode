class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas:
            return -1
        start = 0
        l = len(gas)
        while start < l:
            x = 0
            for i in range(l):
                diff = gas[(start+i)%l] - cost[(start+i)%l]
                x += diff
                if x < 0:
                    start = start + i 
                    break
            if x >= 0:
                return start
            start += 1
        return -1