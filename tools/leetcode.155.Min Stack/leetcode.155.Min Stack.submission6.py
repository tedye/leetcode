class MinStack:
    def __init__(self):
        self.stack = []
        self.minPos = 0
        self.topElement = -1
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        self.topElement += 1
        if self.stack[self.minPos] > x:
            self.minPos = self.topElement
            
    # @return nothing
    def pop(self):
        if self.stack:
            if self.minPos == self.topElement:
                self.topElement -= 1
                del self.stack[-1]
                self.updateMinPos()
            else:
                self.topElement -= 1
                del self.stack[-1]
            
    # @return an integer
    def top(self):
        return self.stack[self.topElement]

    # @return an integer
    def getMin(self):
        return self.stack[self.minPos]

    def updateMinPos(self):
        if self.stack:
            self.minPos = self.stack.index(min(self.stack[:self.topElement + 1]))