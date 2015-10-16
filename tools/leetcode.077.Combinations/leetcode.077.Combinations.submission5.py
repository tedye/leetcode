class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        return [i for i in self.combinations(range(1, n+1),k)]

    def combinations(self,iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield list(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield list(pool[i] for i in indices)