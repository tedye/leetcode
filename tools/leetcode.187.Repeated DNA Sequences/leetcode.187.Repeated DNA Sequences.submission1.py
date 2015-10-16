class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []

        result = set()
        d = set()
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub not in d:
                d.add(sub)
            else:
                result.add(sub)
        return list(result)
        