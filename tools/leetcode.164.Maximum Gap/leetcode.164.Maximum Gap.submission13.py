class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2: return 0
        m = max(num)
        iteration = 0
        while m > 0:
            m //= 2
            iteration += 1
        buckets = [num]
        for i in range(iteration):
            next = [[],[]]
            for bucket in buckets:
                for n in bucket:
                    next[(n >> i) & 1] += [n]
            buckets = next
        res = []
        for bucket in buckets:
            res.extend(bucket)
        Max = 0
        for i in range(len(res)-1):
            Max = max(Max,res[i+1]-res[i])
        return Max
        