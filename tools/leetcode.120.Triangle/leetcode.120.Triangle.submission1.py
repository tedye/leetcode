class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        res = triangle.pop(-1)
        while triangle:
            new_res = triangle.pop(-1)
            for i in range(len(new_res)):
                new_res[i] += min(res[i],res[i+1])
            res = new_res
        return res[0]
        