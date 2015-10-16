class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        re = [gas[i] - cost[i] for i in range(len(gas))]
        
        for i in range(len(gas)):
            x = 0
            temp = re[i:] + re[:i]
            flag = True
            for r in temp:
                x += r
                if x < 0:
                    flag = False
                    break
            if flag:
                return i
        return -1
        