class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        remain = [gas[i] - cost[i] for i in range(len(gas))]
        
        start = 0
        end = len(gas)
        while start < end:
            r = 0
            for i in range(start, start+end):
                r += remain[i%end]
                if r < 0:
                    start = i
                    break
            if r >= 0:
                return start
            start += 1
        return -1
        