class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1 = len(v1)
        l2 = len(v2)
        for i in range(min(l1,l2)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        
        if l1 > l2 and int(v1[l2]) > 0:
            return 1
        elif l2 > l1 and int(v2[l1]) > 0:
            return -1
        else:
            return 0