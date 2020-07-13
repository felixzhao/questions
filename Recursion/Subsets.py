class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Lexicographic (Binary Sorted) Subsets

        Good Solution

        logic
            - create a binay mask, nums's length
            - bit move the mask
                - if '1' get the position
                - add to result

        time  O(N * 2^N)
        space O(N * 2^N)

        """
        n = len(nums)
        res = []
        for i in range(2 ** n, 2 ** (n + 1)):
            mask = bin(i)[3:]
            res.append([nums[j] for j in range(n) if mask[j] == '1'])
        return res