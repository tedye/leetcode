class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): return False
        i = 0
        pos = {(0,0)}
        while pos and i < len(s3):
            temp = set()
            for p in pos:
                if p[0] == len(s2) and p[1] == len(s1):
                    continue
                elif p[0] == len(s2):
                    if s1[p[1]] == s3[i]:
                        temp.add((p[0],p[1]+1))
                elif p[1] == len(s1):
                    if s2[p[0]] == s3[i]:
                        temp.add((p[0]+1,p[1]))
                else:
                    if s1[p[1]] == s3[i]:
                        temp.add((p[0],p[1]+1))
                    if s2[p[0]] == s3[i]:
                        temp.add((p[0]+1,p[1]))
            pos = temp
            i += 1
        return i == len(s3) and (len(s2),len(s1)) in pos
        