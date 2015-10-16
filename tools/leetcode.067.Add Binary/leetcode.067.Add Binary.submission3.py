class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        length = max(len(a),len(b))
        #padding
        res = [""] * (length+1)
        al = list(a)[::-1]
        bl = list(b)[::-1]
        if len(al) < length:
            al.extend(["0"]*(length-len(al)))
        if len(bl) < length:
            bl.extend(["0"]*(length-len(bl)))
            
        pos = 0
        carry = 0
        while pos < length:
            sum = ord(al[pos])+ord(bl[pos])+carry - ord('0') * 2
            carry = sum // 2
            sum %= 2
            res[pos] = chr(ord('0')+sum)
            pos += 1
        if carry:
            res[pos] = chr(ord('0')+carry)
        
        return ''.join(res[::-1])
        