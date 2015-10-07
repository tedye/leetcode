class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        cur = []
        i = 0
        l = len(words)
        curL = 0
        while i < l:
            cur.append(words[i])
            curL += len(words[i])
            if curL+len(cur)-1 > maxWidth:
                cur.pop(-1)
                curL -= len(words[i])
                numSpace = maxWidth - curL
                k = len(cur) - 1
                if k == 0:
                    res.append(cur[0] + ' ' * numSpace)
                else:
                    for j in range(numSpace):
                        cur[j%k] += ' '
                    res.append(''.join(cur))
                curL = 0
                cur = []
                continue
            elif i == l - 1:
                numSpace = maxWidth - curL
                k = len(cur)
                if k == 1:
                    res.append(cur[0] + ' ' * numSpace)
                else:
                    res.append(' '.join(cur) + ' '*(numSpace - len(cur)+1))
            i += 1
        return res     