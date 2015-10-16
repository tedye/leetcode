class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        mapping = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
        temp = 0
        temp += mapping[(n&0xf0000000)>>28]
        temp += mapping[(n&0x0f000000)>>24] << 4
        temp += mapping[(n&0x00f00000)>>20] << 8
        temp += mapping[(n&0x000f0000)>>16] << 12
        temp += mapping[(n&0x0000f000)>>12] << 16
        temp += mapping[(n&0x00000f00)>>8 ] << 20
        temp += mapping[(n&0x000000f0)>>4 ] << 24
        temp += mapping[(n&0x0000000f)    ] << 28
        return temp