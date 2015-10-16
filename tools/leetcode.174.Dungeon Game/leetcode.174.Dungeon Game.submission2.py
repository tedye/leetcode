class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        w = len(dungeon[0])
        h = len(dungeon)
        hp = [[0x7fffffff] * (w+1) for x in range(h+1)]
        hp[-1][w-1] = 1
        hp[h-1][-1] = 1
        for x in range(h - 1, -1, -1):
            for y in range(w - 1, -1, -1):
                hp[x][y] = max(min(hp[x + 1][y], hp[x][y + 1])-dungeon[x][y],1)
        return hp[0][0]     
        