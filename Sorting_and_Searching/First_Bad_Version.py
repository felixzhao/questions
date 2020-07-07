# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        """

        Good Question

        Iterative Binary Search

        logic:
            - similar with 'find peak element'
            - because of left side version is connect with mid
            - so, mid should be include if search left part
            - but mid NOT include when search right part

        key points:
            - l start from 1
            - if mid is bad version, r = mid

        time  O(logN)
        space O(1)

        """
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            print(f'l {l}, r {r}, mid {mid}, isBadVersion(mid) {isBadVersion(mid)}')
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l