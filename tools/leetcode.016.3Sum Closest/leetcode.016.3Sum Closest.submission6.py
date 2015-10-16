class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        l = len(num)
        threshold = 0x7fffffff
        s = 0
        for i in range(l):
            j = i + 1
            k = l - 1
            while j < k:
                sum0 =  num[i] + num[j] + num[k]
                diff = abs(target - sum0)
                if diff == 0: return sum0
                
                if diff < threshold:
                    threshold = diff
                    s = sum0
                
                if sum0 < target:
                    j += 1
                else:
                    k -= 1
                    
        return s
            