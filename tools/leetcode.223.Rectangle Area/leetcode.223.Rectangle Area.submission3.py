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
        # calculate the separate areas
        w1 = C - A
        h1 = D - B
        w2 = G - E
        h2 = H - F
        A1 = w1*h1
        A2 = w2*h2
        if A1 == 0:
            return A2
        if A2 == 0:
            return A1
        # calculate the intersected area
        wi = 0
        if A <= E:
            if E-A < w1:
                wi = min(A+w1 - E,w2)
        else:
            if A - E < w2:
                wi = min(E+w2 - A,w1)
        hi = 0
        if F <= B:
            if B - F< h2:
                hi = min(F + h2 - B,h1)
        else:
            if F - B < h1:
                hi = min(B + h1 - F,h2)
        A3 = wi * hi
        
        return A1+A2-A3
        