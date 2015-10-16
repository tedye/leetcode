class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:return True
        s = s.lower()
        puncset = [',','.',':','\'','\"','?','!',';','/','(',')','[',']','-',' ','@','#','$','%','^','&','*','_','+','~','`','\\','{','}','|','<','>']
        posl = 0
        posr = len(s) - 1
        while posl < posr:
            while posl < len(s) - 1 and s[posl] in puncset:
                posl += 1
            while posr > 0 and s[posr] in puncset:
                posr -= 1
            if s[posr] not in puncset and s[posl] not in puncset and s[posr] != s[posl]:
                return False
            else:
                posr -=1
                posl +=1
        return True