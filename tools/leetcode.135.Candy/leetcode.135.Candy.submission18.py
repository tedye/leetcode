class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if not ratings: return 0
        if len(ratings) == 1: return 1
        ratings.append(ratings[-1])
        candies = 0
        curLevel = 1
        localMaxPos = 0
        localMax = 1
        curPos = 0
        length = len(ratings)
        while curPos < length - 1:
            candies += curLevel
            if ratings[curPos] < ratings[curPos + 1]:
                curLevel += 1
                localMaxPos = curPos + 1
                localMax = curLevel
            elif ratings[curPos] == ratings[curPos + 1]:
                curLevel = 1
                localMaxPos = curPos + 1
                localMax = 1
            else:
                if curLevel == 1:
                    if curPos + 1 - localMaxPos == localMax:
                        localMax += 1
                        candies += (curPos + 1 - localMaxPos)
                    elif curPos + 1 - localMaxPos < localMax:
                        candies += curPos - localMaxPos
                else:
                    curLevel = 1
            curPos += 1
        return candies
        