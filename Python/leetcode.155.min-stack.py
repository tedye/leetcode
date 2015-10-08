class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.minIndex = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.minIndex.append(0)
        else:
            self.stack.append(x)
            if self.stack[self.minIndex[-1]] > x:
                self.minIndex.append(len(self.stack)-1)
            else:
                self.minIndex.append(self.minIndex[-1])

    # @return nothing
    def pop(self):
        self.stack.pop(-1)
        self.minIndex.pop(-1)

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.stack[self.minIndex[-1]]
        