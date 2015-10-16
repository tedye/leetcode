class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.x = []
        for vec in vec2d:
            self.x.extend(vec)
        self.counter = 0
        self.length = len(self.x)

    def next(self):
        """
        :rtype: int
        """
        self.counter += 1
        return self.x[self.counter-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.counter < self.length
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())