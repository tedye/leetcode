class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        a = dict()
        b = set()
        for i,n in enumerate(num):
            if n not in b:
                a[n] = [i]
                b.add(n)
            else:
                a[n].append(i)
        
        for k in b:
            t = target - k
            if t in b:
                if k == t and len(a[k]) == 2:
                    return (a[k][0]+1,a[k][1]+1)
                else:
                    if a[k][0] > a[t][0]:
                        return (a[t][0]+1,a[k][0]+1)
                    else:
                        (a[k][0]+1,a[t][0]+1)
            
        return None
