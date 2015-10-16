class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        if len(citations) == 1 and citations[0] > 0:
            return 1
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] < i+1:
                return i
        return len(citations)
