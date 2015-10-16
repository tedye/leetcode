class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # basically mimic topological sort
        
        # prepare primary data structure to store information
        d = {}
        left = 0
        right = 1
        elements = set(list(''.join(words)))
        for e in elements:
            d[e] = [set(),set()]
        
        # process words and extract relational information 
        queue = [words]
        while queue:
            workingset = queue.pop(0)
            curletter = workingset[0][0]
            letterList = [curletter]
            i = 0
            l = len(workingset)
            nextworkingset = []
            while i < l:
                if workingset[i][0] == curletter:
                    if workingset[i][1:]:
                        nextworkingset += workingset[i][1:],
                    i += 1
                else:
                    if len(nextworkingset) > 1:
                        queue += nextworkingset[:],
                    nextworkingset = []
                    curletter = workingset[i][0]
                    letterList += curletter,
            if len(nextworkingset) > 1:
                    queue += nextworkingset[:],
            
            # update relational information in the primary dict.
            if len(letterList) != len(set(letterList)):
                return ''
            for ind, letter in enumerate(letterList):
                leftelements = set(letterList[:ind])
                rightelements = set(letterList[ind+1:])
                if leftelements&d[letter][right] or rightelements&d[letter][left]:
                    return ''
                d[letter][left] |= set(letterList[:ind])
                d[letter][right]|= set(letterList[ind+1:])
        
        # generate the sequence
        leftside = ''
        rightside = ''
        
        # get rid of free letters first
        for letter in d:
            if not d[letter][left] and not d[letter][right]:
                leftside += letter
        for letter in leftside:
            del d[letter]

        # DEBUG - check dictionary
        # print('---- check dictionary ----')
        # for k in d:
        #     print('<{}> {} <{}>'.format(d[k][left],k,d[k][right]))
        # print('---- check completed  ----')

        while d:
            # get the current leftmost and rightmost letters
            toDel = set()
            newleftside = ''
            newrightside = ''
            for letter in d:
                if not d[letter][left]:
                    newleftside += letter
                    toDel.add(letter)
                if not d[letter][right]:
                    newrightside += letter
                    toDel.add(letter)
            leftside += newleftside
            rightside += newrightside
            # update dictionary
            for letter in toDel:
                del d[letter]

            for letter in d:
                d[letter][left] -= set(newleftside)
                d[letter][right]-= set(newrightside)
        if rightside and leftside[-1]==rightside[-1]:
            return leftside+rightside[::-1][1:]
        return leftside+rightside[::-1]
        