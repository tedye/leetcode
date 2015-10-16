class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:
            return []
        
        result = []
        num.sort()
        num2 = list(set(num))
        num2.sort()
        
        if num.count(0) > 2:
            result.append([0,0,0])

        twos = []
        for n in num2:
            if num.count(n) > 1 and n != 0:
                twos.append(n)

        for n in twos:
            if -2*n in num2:
                result.append(sorted([n,n,-2*n]))


        for i in range(len(num2)-2):
            m = i + 1
            l = len(num2) - 1
            while l > m:
                test = num2[i] + num2[m] + num2[l]
                if test == 0:
                    good = [num2[i], num2[m], num2[l]]
                    good.sort()
                    result.append(good)
                    m += 1
                    l -= 1
                elif test > 0:
                    l -= 1
                else:
                    m += 1
        return result