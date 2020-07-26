# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        Smart Solution (From official answer)

        Question Type:
        - Searching

        logic:
        - start from right top cell
            - if 1 move left
            - else if 0 move down
        - this approach avoid maintain mutiplue points
            - if r, c not move
                - either, next column is answer
                - either, c never moved which means no answer

        time  O(M + N)
        space O(1)
        """
        rows, cols = binaryMatrix.dimensions()
        r = 0
        c = cols - 1
        while r < rows and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                c -= 1
            else:
                r += 1
        return c + 1 if c != cols - 1 else -1
