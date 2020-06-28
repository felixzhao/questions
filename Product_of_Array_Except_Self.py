class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Left and Right product lists
        (magic method)

        logic:
            - left and right array
                - Left
                    - init with all 1
                    - left to right
                    - L[i + 1] = L[i] * Nums[i], i < len(L)
                - right
                    - smilliar with Left
                    - init with all 1
                    - right to left
                    - L[i - 1] = L[i] * Nums[i], i > 0
                - result
                    - res[i] = L[i] * R[i]

        Magic method, what I can do is remember it.

        Key Points:
            - python Range() method
                - Range(end)
                - Range(start, end)
                - Range(start, end, step)
                - e.g.
                >>> list(range(10))
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                >>> list(range(1, 11))
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            - if loop from end to begin of an array
                - Range(start, end, step)
                    - start
                - e.g.
                >>> arr = ['a','b','c','d','e','f']
                >>> list(range(len(arr)))
                [0, 1, 2, 3, 4, 5]
                >>> list(range(len(arr), 0, -1))
                [6, 5, 4, 3, 2, 1]
                >>> list(range(len(arr) - 1, 0, -1))
                [5, 4, 3, 2, 1]
                >>> list(range(len(arr) - 1, -1, -1))
                [5, 4, 3, 2, 1, 0]
            - Another way loop array from right to left
                - e.g.
                >>> list(reversed(range(len(arr))))
                [5, 4, 3, 2, 1, 0]

        time  O(N)
        space O(N)
        """
        l = [1] * len(nums)
        r = [1] * len(nums)
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            l[i] = l[i - 1] * nums[i - 1]
        for j in reversed(range(len(nums) - 1)):
            # print('j ' + str(j))
            r[j] = r[j + 1] * nums[j + 1]
        for i in range(len(res)):
            res[i] = l[i] * r[i]
        # print(l)
        # print(r)
        # print(res)
        return res
