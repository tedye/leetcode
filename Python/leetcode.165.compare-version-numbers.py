class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        while v1 and v2:
            n1 = int(v1.pop(0))
            n2 = int(v2.pop(0))
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        if v1:
            while v1 and int(v1[0]) == 0:
                v1.pop(0)
            if not v1:
                return 0
            else:
                return 1
        if v2:
            while v2 and int(v2[0]) == 0:
                v2.pop(0)
            if not v2:
                return 0
            else:
                return -1
        return 0