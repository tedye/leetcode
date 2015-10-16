class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if not dict: return 0
        
        ndict = set(dict)
        layerNo = 0
        layerS = {start}
        layerE = {end}
        t = layerS&layerE
        notConnectS = False
        notConnectE = False
        while not t and dict:
            temp = set()
            for j in layerS:
                self.diff1(j,dict,temp)
            if not temp:
                notConnectS = True
                break
            else: layerS = temp
            dict = dict - layerS
            layerNo += 1
            if layerS & layerE: 
                break
            temp = set()
            for j in layerE:
                self.diff1(j,ndict,temp)
            if not temp:
                notConnectE = True
                break
            else: layerE = temp
            layerE = temp
            layerNo += 1
            t = layerS & layerE
            if t: break
            ndict = ndict - layerE
            
        if not dict or notConnectS or notConnectE:
            return 0 
        return layerNo + 1
                    
    def diff1(self,a,dict,temp):
        # return True if two words a and b only diff by one letter
        
        w = 'abcdefghijklmnopqrstuvwxyz'
        wordLen = len(a)
        for i in range(wordLen):
            part1 = a[:i] 
            part2 = a[i+1:]
            for j in w:
                if a[i] != j:
                    nextWord = part1 + j + part2
                    if nextWord in dict:
                        temp.add(nextWord)

        