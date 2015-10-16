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

        buckets = [[0x7fffffff,-1,[]] for _ in range(bucket_num)] 
        for n in num:
            pos = (n - Min) >> x
            buckets[pos][0] = min(buckets[pos][0],n)
            buckets[pos][1] = max(buckets[pos][1],n)
            buckets[pos][2] += [n]

        Max = 0
        i = 0
        localmax = buckets[0][1]
        while i < len(buckets):
            while not buckets[i][-1]:
                i += 1
            Max = max(Max, buckets[i][0] - localmax)
            localmax = buckets[i][1]
            i += 1
        return Max
        