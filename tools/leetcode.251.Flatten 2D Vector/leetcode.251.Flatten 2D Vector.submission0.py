class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.x = 0
        self.y = 0
        self.vec = [i for i in vec2d if i]
        self.nextone = None
        try:
            self.nextone = self.vec[self.x][self.y]
        except:
            pass

    def next(self):
        """
        :rtype: int
        """
        temp = self.nextone
        self.y += 1
        if self.y == len(self.vec[self.x]):
            self.y = 0
            self.x += 1
        self.nextone = None
        try:
            self.nextone = self.vec[self.x][self.y]
        except:
            pass
        
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nextone != None
        
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())