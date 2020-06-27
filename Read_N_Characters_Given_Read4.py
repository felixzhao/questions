"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)

        time  O(N)
        space O(1)

        idea:
        - keep idx for the count of result
        - read4 to buf4 and set to result buf by loop
        - decrease n by loaded count

        key points:
        - must check read4() result count, if <= 0 mean all done, then return
        - set buf use idx is enough
        - do not remember update n and idx

        why have question like this?
        Actually, this question may be more practical than it looks like at your first glimpse.

        In reality, hw or system may have constraints for read from file system. eg. hardeware DMA engine may fetch data 128 bytes from disk. another example is that loading 4-bytes in aligned ddr should be obviously faster than load 1 byte 4 times. It is exactly same as read4 problem.
        """
        idx = 0
        while n > 0:
            buf4 = [''] * 4
            i = read4(buf4)
            if i <= 0:
                return idx
            for j in range(min(i, n)):
                buf[idx] = buf4[j]
                idx += 1
                n -= 1
        return idx

