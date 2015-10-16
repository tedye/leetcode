class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        if not words: return
        res = []
        cur = []
        length = 0
        for w in words:
            if length + len(w) < L:
                length += len(w)+1
                cur += [w+' ']
            elif length + len(w) == L:
                cur += [w]
                res += [''.join(cur)]
                cur = []
                length = 0
            else:
                if len(cur) == 1:
                    cur += [' ' * (L-length)]
                else:
                    cur[-1] = cur[-1][:-1]
                    spaces = L - length + 1
                    i = 0
                    while spaces:
                        cur[i] += ' '
                        i += 1
                        if i == len(cur) - 1:
                            i = 0
                        spaces -= 1
                res += [''.join(cur)]
                cur = [w+' ']
                length = len(w) + 1
                if length == L + 1:
                    res += [w]
                    cur = []
                    length = 0
        if cur:
            cur += [' ' * (L-length)]
            res += [''.join(cur)]
        return res
                
                