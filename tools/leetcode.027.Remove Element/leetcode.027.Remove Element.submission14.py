class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A: return 0
        temp = sorted(A)
        for item in temp:
            if item == elem:
                A.remove(elem)
        return len(A)
                