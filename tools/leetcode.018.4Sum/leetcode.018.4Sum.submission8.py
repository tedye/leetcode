class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        l = len(num)
        res = []
        i = 0
        while i < l:
            j = i + 1
            while j < l:
                k = j + 1
                e = l - 1
                while k < e:
                    sum0 = num[i] + num[j] + num[k] + num[e]
                    if sum0 == target:
                        res += [[num[i], num[j], num[k], num[e]]]
                    
                    if sum0 < target:
                        k += 1
                    elif sum0 > target:
                        e -= 1
                    else:
                        k += 1
                        while k<e and num[k-1] == num[k]:
                            k += 1
                j += 1
                while j<l and num[j-1] == num[j]:
                            j += 1
            i += 1
            while i<l and num[i-1] == num[i]:
                            i += 1
        return res