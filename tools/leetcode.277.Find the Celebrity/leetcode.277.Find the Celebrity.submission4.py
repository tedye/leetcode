# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # first attempt - use array to record
        # if candidates[i] is a possible celebrity
        '''
        candidates = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                if knows(i,j):
                    if candidates[j] != -1:
                        candidates[j] += 1
                    candidates[i] = -1
                if knows(j,i):
                    if candidates[i] != -1:
                        candidates[i] += 1
                    candidates[j] = -1
        try:
            return candidates.index(n-1)
        except ValueError:
            return -1
        # failed TLE
        '''
        
        # try single set
        candidates = set(range(n))
        for i in range(n):
            for j in range(i+1,n):
                if i in candidates and knows(i,j):
                    candidates.remove(i)
                if j in candidates and knows(j,i):
                    candidates.remove(j)
        for can in candidates:
            flag = True
            for i in range(n):
                if not knows(i,can) and i != can:
                    flag = False
                    break
            if flag:
                return can
        return -1
        