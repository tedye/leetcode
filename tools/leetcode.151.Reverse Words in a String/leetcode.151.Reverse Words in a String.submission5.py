class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if not s:
            return ''
        temp = []
        word = ''
        s += ' '
        for i in s:
            if i == ' ':
                if word != '':
                    temp.append(word)
                    word = ''
                    continue
            else:
                word += i
        return " ".join(temp[::-1])