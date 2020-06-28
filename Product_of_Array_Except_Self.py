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

        time  O(N)
        space O(N)
        """
        l = [1] * len(nums)
        r = [1] * len(nums)
        res = [1] * len(nums)
        for i in range(len(nums) - 1):
            l[i + 1] = l[i] * nums[i]
        for j in range(len(nums) - 1, 0, -1):
            # print('j ' + str(j))
            r[j - 1] = r[j] * nums[j]
        for i in range(len(res)):
            res[i] = l[i] * r[i]
        # print(l)
        # print(r)
        # print(res)
        return res
