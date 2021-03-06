class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.s1.append(x)

    # @return nothing
    def pop(self):
        if self.s2:
            self.s2.pop(-1)
        elif self.s1:
            while self.s1:
                self.s2.append(self.s1.pop(-1))
            self.s2.pop(-1)

    # @return an integer
    def peek(self):
        if self.s2:
            return self.s2[-1]
        elif self.s1:
            while self.s1:
                self.s2.append(self.s1.pop(-1))
            return self.s2[-1]
        return -1
        

    # @return an boolean
    def empty(self):
        return not self.s1 and not self.s2
        