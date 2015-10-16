class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2: return 0
        m = max(num)
        iteration = 0
        while m > 0:
            m >>= 4
            iteration += 1
        buckets = [num]
        for i in range(iteration):
            next = [[] for _ in range(16)]
            for bucket in buckets:
                for n in bucket:
                    next[(n >> i*4) & 15] += [n]
            buckets = next
        cur = None
        Max = 0
        for bucket in buckets:
            for n in bucket:
                if not cur:
                    cur = n
                else:
                    Max = max(Max,n - cur)
                    cur = n
        return Max
        