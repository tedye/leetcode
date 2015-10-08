class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings: return 0
        candies = [1] * len(ratings)
        
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
        res = candies[-1]
        for i in range(2,len(ratings)+1):
            temp = candies[-i]
            if ratings[-i] > ratings[-i+1]:
                candies[-i] = candies[-i+1]+1
            else:
                candies[-i] = 1
            res += max(temp, candies[-i])
        return res