class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2: return 0
        if len(num) == 2: return abs(num[0]-num[1])
        Max = max(num)
        Min = min(num)
        x = 0
        bucket_len = max((Max - Min) // (len(num) - 1),1)
        while bucket_len > 0:
            x += 1
            bucket_len >>= 1
        bucket_num = ((Max - Min) >> x) + 1

        buckets = [[] for _ in range(bucket_num)] 
        for n in num:
            buckets[(n - Min) >> x] += [n]

        localmax = max(buckets[0])
        Max = 0
        i = 0
        while i < len(buckets):
            while not buckets[i]:
                i += 1
            Max = max(Max, min(buckets[i]) - localmax)
            localmax = max(buckets[i])
            i += 1
        return Max
        