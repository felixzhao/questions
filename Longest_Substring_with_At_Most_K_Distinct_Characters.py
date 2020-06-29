from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        time  O(N)
        space O(1)

        smart way

        logic
        (Sliding Window + Counter(save count of char))
            - slideing window by two pointers
                - one figure start
                - another figure slide window end
            - move window end, count all char in Counter
            - if distnct char count > k
                - move start

        Python tech:
        - Counter: a dict save obj and count
https://docs.python.org/2/library/collections.html#collections.Counter
        - enumerate: effect way to do the loop
https://docs.python.org/2/library/functions.html#enumerate

        """
        counter = Counter()
        res, i, n = 0, 0, 0
        for j, c in enumerate(s):
            if counter[c] == 0:  # never seen before
                n += 1
            counter[c] += 1
            while n > k:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    n -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
