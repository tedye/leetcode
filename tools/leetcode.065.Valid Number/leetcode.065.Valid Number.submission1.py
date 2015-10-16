class Solution:
    # @param s, a string
    # @return a boolean
    def __init__(self):
        self.next_state = [ [-1, 0, 1, 3, 2,-1],
                            [-1,-1,-1, 3, 2,-1],
                            [-1,-1,-1, 4,-1,-1],
                            [-1, 8,-1, 3, 4, 5],
                            [-1, 8,-1, 4,-1, 5],
                            [-1,-1, 6, 7,-1,-1],
                            [-1,-1,-1, 7,-1,-1],
                            [-1, 8,-1, 7,-1,-1],
                            [-1, 8,-1,-1,-1,-1]]

    def isNumber(self, s):
        state = 0
        for i in s:
            sig = 0
            if i == ' ':
                sig = 1
            elif i == '+' or i == '-':
                sig = 2
            elif '0' <= i <= '9':
                sig = 3
            elif i == '.':
                sig = 4
            elif i == 'e' or i == 'E':
                sig = 5
            state = self.next_state[state][sig]
            if state == -1:
                return False
        return state in {3,4,7,8}
        