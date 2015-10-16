class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strings:
            if len(s) not in d:
                d[len(s)] = [s]
            else:
                d[len(s)] += s,
        result = []
        for l in d:
            tempd = {}
            for word in d[l]:
                x = tuple([(ord(word[j]) - ord(word[0])) % 26 for j in range(l)])
                if x not in tempd:
                    tempd[x] = [word]
                else:
                    tempd[x] += word,
            result.extend([sorted(tempd[key]) for key in tempd])
        return result
        