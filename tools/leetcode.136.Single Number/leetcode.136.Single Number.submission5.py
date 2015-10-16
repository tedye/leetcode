class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        number = 0
        for int in A:
            number ^= int
        return number