class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2: return 0
        Max = 0
        Min = 0x7fffffff
        for i in num:
            Max = max(i,Max)
            Min = min(i,Min)

        bucket_len = max((Max - Min) // (len(num) - 1),1)
        bucket_num = (Max - Min) // bucket_len + 1
        buckets = [[] for _ in range(bucket_num)]
        for i in num:
            buckets[(i - Min) // bucket_len] += [i]
        Max = 0
        i = 0
        while not buckets[i]:
            i += 1
        localmax = max(buckets[i])
        i += 1
        while i < bucket_num:
            while not buckets[i]:
                i += 1
            Max = max(Max,min(buckets[i]) - localmax)
            localmax = max(buckets[i])
            i += 1

        return Max
        