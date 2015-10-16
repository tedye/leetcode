import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_number = 0

        heap = []
        heapq.heappush(heap, 1)
        check = set()
        check.add(1)
        for _ in range(n):
            ugly_number = heapq.heappop(heap)
            if ugly_number * 2 not in check:
                heapq.heappush(heap, ugly_number * 2)
                check.add(ugly_number * 2)
            if ugly_number * 3 not in check:
                heapq.heappush(heap, ugly_number * 3)
                check.add(ugly_number * 3)
            if ugly_number * 5 not in check:
                heapq.heappush(heap, ugly_number * 5)
                check.add(ugly_number * 5)
        return ugly_number