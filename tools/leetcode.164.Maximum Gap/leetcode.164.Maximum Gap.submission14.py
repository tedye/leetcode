class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2: return 0
        m = max(num)
        iteration = 0
        while m > 0:
            m >>= 1
            iteration += 1
        buckets = [num]
        for i in range(iteration):
            next = [[],[]]
            for bucket in buckets:
                for n in bucket:
                    next[(n >> i) & 1] += [n]
            buckets = next
        cur = 0
        if buckets[0]:
            cur = buckets[0][0]
        else:
            cur = buckets[1][0]
        Max = 0
        for bucket in buckets:
            for n in bucket:
                    Max = max(Max,n - cur)
                    cur = n
        return Max
        