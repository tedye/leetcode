class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        result = []
        if not strs: return result
        if len(strs) ==  1: return result
        
        reference = {}
        for word in strs:
            temp = [0] * 26
            for letter in word:
                temp[ord(letter) - ord('a')] += 1
            key = ''.join([chr(ord('a') + i) + str(temp[i]) for i in range(26)])
            if key not in reference:
                reference[key] = [word]
            else:
                reference[key].append(word)
        for key in reference:
            if len(reference[key]) > 1:
                result.extend(reference[key])
        return result
                
        
        
        