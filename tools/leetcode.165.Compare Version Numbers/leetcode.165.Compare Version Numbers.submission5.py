class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        a1 = [int(n) for n in version1.split('.')]
        a2 = [int(n) for n in version2.split('.')]
        
        short = min(len(a1),len(a2))
        for i in range(short):
            if a1[i] < a2[i]:
                return -1
            elif a1[i] > a2[i]:
                return 1
        if len(a1) == len(a2):
            return 0
        elif len(a1) > len(a2):
            if sum(a1[short:]) != 0:
                return 1
            else:return 0
        else:
            if sum(a2[short:]) != 0:
                return -1
            else: return 0