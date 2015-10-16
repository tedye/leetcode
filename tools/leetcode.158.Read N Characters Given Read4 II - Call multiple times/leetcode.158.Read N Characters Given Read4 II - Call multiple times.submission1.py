# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buffer_size = 0
        self.offset = 0
        self.buffer = [None] * 4
    
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        read_bytes = 0
        eof = False
        while not eof and read_bytes < n:
            if self.buffer_size == 0:
                size = read4(self.buffer)
            else:
                size = self.buffer_size
            if self.buffer_size == 0 and size < 4:
                eof = True   
            bytes = min(n - read_bytes, size)
            for i in range(bytes):
                buf[read_bytes + i] = self.buffer[self.offset + i]
            self.offset = (self.offset + bytes) % 4
            self.buffer_size = size - bytes
            read_bytes += bytes
        return read_bytes