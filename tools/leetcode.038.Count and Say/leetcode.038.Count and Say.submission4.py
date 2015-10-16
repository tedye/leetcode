class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        # attempt one - build a generator
        start = '1'
        for i in range(n-1):
            res = ""
            current = 0
            end = len(start)
            while current < end:
                token = start[current]
                count = 1
                current += 1
                while current < end and start[current] == token:
                    count += 1
                    current += 1
                res += str(count)+token
            start = res
        return start
 
            