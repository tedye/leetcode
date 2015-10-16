class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        pos = len(digits) - 1
        overflow = False
        while digits[pos] == 9:
            digits[pos] = 0
            if pos == 0:
                overflow = True
                break
            else:
                pos -= 1

        if overflow:
            results = [1] + digits
            return results
        else:
            digits[pos]+=1

            return digits