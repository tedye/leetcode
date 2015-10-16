class MinStack:
    def __init__(self):
        self.stack = []
        self.m = None
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.m:
            self.m = x
        elif self.m > x:
            self.m = x

    # @return nothing
    def pop(self):
        res = self.stack.pop(-1)
        if res == self.m and self.stack:
            self.m = min(self.stack)
        elif not self.stack:
            self.m = None

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.m
        