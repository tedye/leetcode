# The read4 API is already defined for you.# @param buf, a list of characters# @return an integer# def read4(buf):class Solution(object):    def read(self, buf, n):        """        :type buf: Destination buffer (List[str])        :type n: Maximum number of characters to read (int)        :rtype: The number of characters read (int)        """        read_bytes = 0        eof = False        temp = [''] * 4        while not eof and read_bytes < n:            size = read4(temp)            if size < 4:                eof = True            bytes = min(n - read_bytes, size)            for i in range(bytes):                buf[read_bytes + i] = temp[i]            read_bytes += bytes        return read_bytes