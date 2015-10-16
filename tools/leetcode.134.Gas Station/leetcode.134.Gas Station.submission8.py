class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if not gas:
            return -1
        length = len(gas)
        surplus = [gas[i] - cost[i] for i in range(length)]
        if sum(surplus) < 0:
            return -1
        i = 0
        while i <= length - 1:
            remain = 0
            for j in range(i, i + length):
                remain += surplus[j%length]
                if remain < 0 :
                    i = j
                    break
            if remain >= 0:
                return i
            i += 1
        return -1