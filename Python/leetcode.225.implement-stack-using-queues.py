class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.size = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q1.append(x)
        for i in range(self.size):
            self.q1.append(self.q2.pop(0))
        self.size += 1
        self.q2 = self.q1
        self.q1 = []

    # @return nothing
    def pop(self):
        if self.q2:
            self.size -= 1
            return self.q2.pop(0)

    # @return an integer
    def top(self):
        if self.q2:
            return self.q2[0]

    # @return an boolean
    def empty(self):
        return self.size == 0
        