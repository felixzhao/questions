# The read4 API is already defined for you.
# def read4(buf: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = []

    def read(self, buf: List[str], n: int) -> int:
        """
        -What is the difference between call once and call multiple times?
            - Think that you have 4 chars "a, b, c, d" in the file, and you want to call your function twice like this:
                - read(buf, 1); // should return 'a'
                - read(buf, 3); // should return 'b, c, d'
                - All the 4 chars will be consumed in the first call. So the tricky part of this question is how can you preserve the remaining 'b, c, d' to the second call.

        - What will happen if you call read multi times?
            - Your input
                - "abcefghijklm"
                - [4,4,4]
            - Your answer
                - ["abce","fghi","jklm"]

        - What is the Key point of this question?
            - When n < 4 in read(buf, n), e.g. 1. How can we send the 3 left chrs in next call?

        Solution:
            - from https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/269/discuss/193873/Most-elegant-and-simple-solution-in-Python
            - idea:
                - two round
                    - 1. load from read4 to global queue
                    - 2. put n item from queue to buf, if n < 4 then rest part keep in queue for next read

        Key Points:
            - must check read4(buf) return 0 if no more data to read
            - add buf4 to queue must use buf4[:i], because buf4 init with 4 empty chr
                - skip following empty chr is nessary, when i < 4
            - get value from queue must use self.q.pop(0)
                - As python array default pop() return last element
            - add to queue use '+' join to array is works fine
        """
        idx = 0
        buf4 = [''] * 4
        while idx < n:
            if self.q:
                buf[idx] = self.q.pop(0)
                idx += 1
            else:
                i = read4(buf4)
                if i <= 0:
                    break
                self.q += buf4[:i]
        return idx
