class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        if not words:
            return []
        
        i = 0
        l = len(words)
        res = []
        while i < l:
            count = 0
            combine = []
            while i < l and count+len(words[i]) <= maxWidth:
                count += len(words[i])+1
                combine.append(words[i])
                i += 1
            count -= 1
            if len(combine) == 1:
                res.append(combine[0] + ' ' * (maxWidth - count))
                continue
            length = len(combine) - 1
            x = [' '] * length
            spaces = maxWidth - count
            fi = []
            if i == l:
                fi = [''] * (2*len(combine))
                x.append(' '*spaces)
            else:
                fi = [''] * (2*len(combine)-1)
                for k in range(spaces):
                    x[k%length] += ' '
            fi[::2] = combine
            fi[1::2] = x
            res.append(''.join(fi))
        return res
        
        