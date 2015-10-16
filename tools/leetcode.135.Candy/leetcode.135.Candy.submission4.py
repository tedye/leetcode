class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        if not ratings: return 0
        candies = [1]
        
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies.append(candies[-1]+1)
            else:
                candies.append(1)
        res = candies[-1]
        for i in range(2,len(ratings)+1):
            if ratings[-i] > ratings[-i+1]:
                x = candies[-i+1]+1
            else:
                x = 1
            res += max(x, candies[-i])
            candies[-i] = x
        return res
                
                    
        
        