class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        w1 = C-A
        h1 = D-B
        w2 = G-E
        h2 = H-F
        A1 = w1*h1
        A2 = w2*h2
        if A1 == 0:
            return A2
        if A2 == 0:
            return A1
        w = 0
        h = 0
        if A <= E <= C:
            w = min(C-E, w2)
        if E <= A <= G:
            w = min(G-A, w1)
        
        if B <= F <= D:
            h = min(D-F, h2)
        if F <= B <= H:
            h = min(H-B, h1)
            
        return A1+A2- w * h
        